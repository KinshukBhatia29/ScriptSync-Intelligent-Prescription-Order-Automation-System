# ScriptSync - Intelligent Prescription Order Automation System

## 📌 Overview
ScriptSync is an **AI-powered medical inventory management system** that automates prescription processing using **OCR, NLP, and a smart validation engine**. The system extracts and validates handwritten prescriptions, matches medicines with inventory, and facilitates order management, ensuring accuracy and efficiency in pharmaceutical operations.

## 🚀 Features
- **OCR-Based Prescription Scanning** (Tesseract OCR/Google Cloud Vision)
- **NLP-Powered Medicine Extraction & Validation** (spaCy/BERT & Llama API)
- **Medical Inventory Management** (Stock tracking, medicine search, alerts)
- **Automated Order Creation & Cart System**
- **User Authentication & Role-Based Access**
- **Real-Time Inventory Updates**
- **Interactive Dashboard for Insights & Analytics**
- **RESTful API for Seamless Integration**

## 🏗️ System Architecture
```
User Interface (React.js) → API Gateway (Flask/Django or Node.js) → Database (PostgreSQL/MySQL/Firebase)
                      ↓                                      ↓
        OCR & NLP Engine (Tesseract/Google Cloud Vision + spaCy/BERT) → Medicine Validation (Llama API)
```

## 🛠️ Tech Stack
### **Frontend:**
- React.js (Next.js optional)
- Tailwind CSS / Bootstrap for UI

### **Backend:**
- Flask / Django or Node.js (Express.js)
- REST API for communication

### **Database:**
- PostgreSQL / MySQL / Firebase
- Redis (for caching, optional)

### **AI/ML:**
- Tesseract OCR / Google Cloud Vision
- spaCy / BERT for NLP
- Llama API for validation



## 🎯 Roadmap
- [ ] Enhance OCR accuracy with custom ML models
- [ ] Implement voice-based prescription input
- [ ] Add AI-powered drug interaction warnings
- [ ] Enable multi-language prescription processing

## 💡 Future Scope
- AI-driven fraud detection in prescriptions
- Blockchain-based prescription security
- Integration with pharmacy ERP systems

## 🤝 Contributing
We welcome contributions! Follow these steps:
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit changes and push (`git push origin feature-xyz`)
4. Open a Pull Request


## 👩‍💻 Author
**Kinshuk Bhatia**  
📧 nhatiakinshuk29.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kinshuk-bhatia-34a62a259) | [GitHub](https://github.com/KinshukBhatia29)

---
💙 *If you found this project helpful, give it a ⭐ on GitHub!*
