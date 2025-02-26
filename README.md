# ScriptSync: Intelligent Prescription Order Automation System

## 📌 Overview
ScriptSync is an AI-powered **prescription order automation system** that extracts, processes, and validates handwritten prescriptions using **OCR and NLP**. It integrates **inventory management**, **order creation**, and **medicine validation** into a seamless workflow, reducing errors and enhancing efficiency.

## 🏗 System Architecture
The system comprises the following components:

1. **Frontend (React.js)**
   - User-friendly dashboard for scanning prescriptions.
   - Cart functionality for adding medicines from prescriptions.
   - Order validation and checkout.

2. **Backend (Flask/Django/Node.js)**
   - API for text extraction and NLP processing.
   - Database management for medicine inventory and orders.
   - Integration with external medicine validation APIs (e.g., Llama API).

3. **OCR & NLP Module**
   - Uses **Tesseract OCR/Google Cloud Vision** for text extraction.
   - **spaCy/BERT** for entity recognition and medicine matching.

4. **Database (PostgreSQL/MySQL/Firebase)**
   - Stores patient orders, inventory details, and extracted prescriptions.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
  git clone https://github.com/KinshukBhatia29/ScriptSync-Intelligent-Prescription-Order-Automation-System.git
  cd ScriptSync-Intelligent-Prescription-Order-Automation-System
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r backend/requirements.txt
npm install --prefix frontend
```

### 4️⃣ Set Up Environment Variables
Create a **.env** file in the backend directory with the following:
```
FLASK_APP=app.py
DATABASE_URL=<your_database_url>
LLAMA_API_KEY=<your_llama_api_key>
```

---

## 🔧 Running the Application

### Start the Backend
```bash
cd backend
python app.py  # Flask/Django backend
```

### Start the Frontend
```bash
cd frontend
npm start
```

---

## 🔬 Key Features
- **Prescription Scanning** 📷: Extracts text from handwritten prescriptions.
- **Medicine Validation** 🏥: Ensures prescribed drugs exist in the database.
- **Cart & Order System** 🛒: Users can add medicines to the cart and place orders.
- **Inventory Management** 📦: Tracks medicine availability in real-time.
- **NLP Processing** 🧠: Identifies drug names, dosage, and instructions.

---

## 📚 API Endpoints
| Endpoint             | Method | Description                     |
|---------------------|--------|---------------------------------|
| `/extract-text`     | POST   | Extracts text from prescription |
| `/validate-medicine`| POST   | Checks if medicine exists       |
| `/create-order`     | POST   | Adds a new order to database    |
| `/get-inventory`    | GET    | Fetches available medicines     |

---

## 🛠 Future Enhancements
- **Voice-based prescription input.**
- **Blockchain-based prescription validation.**
- **AI-driven dosage recommendations.**

---

## 📝 Contribution Guidelines
1. Fork the repository.
2. Create a new branch.
3. Commit changes and push to GitHub.
4. Submit a pull request.

---

## 📩 Contact
For any queries, reach out at: **kinshukbhatia29@gmail.com**

