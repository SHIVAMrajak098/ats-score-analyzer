<h1 align="center">🧠 AI Resume Analyzer</h1>
<p align="center">
  Analyze your resume against job descriptions using AI & BERT. Get similarity scores, keyword insights, and personalized suggestions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Groq-LLM-green">
  <img src="https://img.shields.io/badge/Resume%20Analysis-AI%20Powered-brightgreen">
</p>

---

## 🚀 Features

- 📄 Upload **Resume (PDF)**
- 💼 Paste **Job Description**
- 🤖 Get **AI-Powered Feedback** using Groq (LLaMA 3)
- 📈 **BERT-based ATS Score** (semantic similarity)
- 📌 **Keyword Match** – see what’s missing!
- 🔮 **Hiring Probability** estimate
- 📥 Downloadable full **report**
- 🧠 Built with **Streamlit**, **sentence-transformers**, and **Groq LLM**

---

## 🖼️ App Preview

### 📍 Main Interface
![Main UI](screenshots/Screenshot%202025-06-17%20162531.png)

### 📍 Job Description Input & Score Output
![Job Description](screenshots/Screenshot%202025-06-17%20162618.png)

### 📍 Keyword Analysis & Final Verdict
![Keyword Match](screenshots/Screenshot%202025-06-17%20162642.png)




---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/Mac

pip install -r requirements.txt 

🔐 Setup API Key
Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

▶️ Run the App

streamlit run main.py

App will open in your browser at http://localhost:8501




## 📦 Tech Stack

Python 3.10+

Streamlit

pdfminer.six

sentence-transformers

scikit-learn

python-dotenv

Groq API (LLaMA-3.3-70b)






