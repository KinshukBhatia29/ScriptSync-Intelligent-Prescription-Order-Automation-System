import os
import cv2
import numpy as np
import pytesseract
import torch
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from transformers import BertTokenizerFast, BertForMaskedLM
import psycopg2  # For PostgreSQL database
import requests  # To call Llama API
from PIL import Image

app = Flask(_name_)

# Load trained OCR Model & BERT Model
ocr_model = load_model("prescription_classification_model_CNRR.keras")
bert_model = BertForMaskedLM.from_pretrained("output_model")
tokenizer = BertTokenizerFast.from_pretrained("output_tokenizer")

# Load Digit Recognition Model
digit_model = load_model("digit_recognition_model.h5")

# Connect to PostgreSQL Database
conn = psycopg2.connect(
    dbname="pharmacy_db",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Load Kaggle Medicine Database
df_medicines = pd.read_csv('/kaggle/input/medicine-dataset/medicines.csv')

# Llama API for Medicine Validation
LLAMA_API_URL = "https://your-llama-api-endpoint.com"
LLAMA_API_KEY = "your_llama_api_key"


# Preprocess Image for OCR
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 32))
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img


# Extract Text with OCR
def extract_text_with_ocr(image_path):
    preprocessed_image = preprocess_image(image_path)
    img = Image.fromarray(preprocessed_image)
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text.strip()


# Validate Medicine Names using Llama API
def validate_medicine_with_llama(medicine_name):
    headers = {"Authorization": f"Bearer {LLAMA_API_KEY}"}
    payload = {"query": medicine_name}
    response = requests.post(LLAMA_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("validated_name", medicine_name)
    else:
        return medicine_name


# Match Extracted Medicines with Kaggle Database
def match_medicine(medicine_name):
    matched_meds = df_medicines[df_medicines["Medicine_Name"].str.contains(medicine_name, case=False, na=False)]
    return matched_meds.to_dict(orient="records") if not matched_meds.empty else None


# Recognize Handwritten Digits for Quantity
def recognize_quantity(image):
    image = cv2.resize(image, (28, 28))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=[0, -1])  # Add batch and channel dims
    prediction = digit_model.predict(image)
    return np.argmax(prediction)


# Process Prescription API
@app.route("/process_prescription", methods=["POST"])
def process_prescription():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_path = "temp_image.png"
    image.save(image_path)

    # Extract Text with OCR
    extracted_text = extract_text_with_ocr(image_path)

    # Tokenize & Process with BERT Model
    tokens = tokenizer(extracted_text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = bert_model(**tokens)

    # Extract Predicted Medicine Names
    predicted_medicines = tokenizer.batch_decode(output.logits.argmax(dim=-1), skip_special_tokens=True)

    # Validate with Llama API
    validated_medicines = [validate_medicine_with_llama(med) for med in predicted_medicines]

    # Match Medicines in Kaggle Database
    matched_medicines = {med: match_medicine(med) for med in validated_medicines}

    # Recognize quantity (assume each medicine has a digit nearby in the image)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    quantities = {}
    for med, _ in matched_medicines.items():
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if 10 < w < 50 and 10 < h < 50:  # Likely a digit region
                digit_roi = thresholded[y:y + h, x:x + w]
                quantity = recognize_quantity(digit_roi)
                quantities[med] = quantity
                break  # Assume one quantity per medicine

    # Store Prescription in Database
    cursor.execute("INSERT INTO prescriptions (text, medicines) VALUES (%s, %s)", (extracted_text, str(quantities)))
    conn.commit()

    return jsonify({"extracted_text": extracted_text, "medicines": quantities})


# Fetch Orders API (For React Frontend)
@app.route("/get_orders", methods=["GET"])
def get_orders():
    cursor.execute("SELECT * FROM prescriptions ORDER BY id DESC")
    orders = cursor.fetchall()
    return jsonify(orders)


if _name_ == "_main_":
    app.run(debug=True)