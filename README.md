# **MANTHAN: AI-Powered Medical Knowledge Extractor**

## 📌 **Project Overview**

MANTHAN is an AI-powered medical assistant designed to **diagnose diseases, summarize medical reports, and analyze YouTube medical lectures**. By integrating **Deep Learning**, **Natural Language Processing (NLP)**, and **Streamlit**, this project enhances medical data accessibility and decision-making.

## 🔥 **Key Features**

- 🩺 **AI Chatbot:** Answers medical queries using **Llama 3.2 (Ollama LLM)**.
- 🏥 **Medical Report Summarization:** Extracts and summarizes PDFs using **NLP techniques**.
- 🎗️ **Breast Cancer Detection:** Identifies potential malignancies from **mammogram images**.
- 🦠 **Malaria Detection:** Uses **Deep Learning** to detect **malaria from blood smear images**.
- 🎥 **YouTube Medical Lecture Summarization:** Summarizes key points from **YouTube medical videos**.

## 🛠 **Tech Stack**

- **Python**: Core programming language
- **Streamlit**: For building an intuitive and interactive UI
- **TensorFlow & Keras**: Deep learning models for disease detection
- **Ollama (Llama 3.2)**: AI-powered chatbot for medical queries
- **PDFPlumber**: Extracts text from medical reports
- **YouTube Transcript API & Transformers**: Summarizes medical lectures

## 🚀 **How It Works**

1. **User Uploads an Image (Mammogram/Blood Smear), PDF, or YouTube Link**
2. **AI Model Processes the Input:**
   - **Image → Deep Learning Model** analyzes it for disease detection.
   - **PDF/YouTube Link → NLP Model** extracts and summarizes content.
   - **Chatbot → LLM Model** responds to medical queries.
3. **Results Are Displayed in an Easy-to-Read Format**

## 📂 **Folder Structure**

```
MANTHAN/
│── modules/
│   ├── breast_cancer_detection.py  # CNN-based model for breast cancer detection
│   ├── malaria_detection.py        # Deep Learning model for malaria detection
│   ├── pdf_summary.py              # Extracts and summarizes medical reports
│   ├── youtube_summary.py          # Summarizes medical YouTube lectures
│── app.py                          # Main application integrating all modules
│── requirements.txt                 # List of dependencies
│── README.md                        # Project documentation
```

## 📥 **Installation & Setup**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/your-repo/MANTHAN.git
cd MANTHAN
```

### **Step 2: Set Up Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Run the Application**

```bash
streamlit run app.py
```

## 🎯 **Usage Guide**

1. **Navigate the sidebar** to select a feature (Chatbot, Disease Detection, or Summarization).
2. **Upload medical images, PDFs, or enter a YouTube link**.
3. **Get instant results** displayed with confidence scores and insights.

## 🔍 **Future Enhancements**

- 🏥 **Expand Disease Detection** to cover **pneumonia, skin cancer, and diabetic retinopathy**.
- 🗣️ **Voice-Enabled Chatbot** for hands-free medical assistance.
- 🌍 **Multilingual Support** for non-English medical reports and videos.

## 🤝 **Contributors**

- **[Harsh Jain]** – AI Engineer & Developer
- **Open Source Contributions** – Welcomed!

## 📜 **License**

This project is **open-source** and available under the **MIT License**.

---

🚀 AcuMed\*\* is built to revolutionize AI-driven medical assistance. Join us in making healthcare smarter!\*\*

