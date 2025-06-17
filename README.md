# 🧠 AI Resume Analyzer

An AI-powered resume analyzer that evaluates resumes against job descriptions using ATS similarity, keyword matching, and personalized feedback via Groq LLaMA-3.

## 🚀 Features

- 📄 Upload PDF Resume
- 💼 Paste Job Description
- 🤖 AI Evaluation (LLaMA-3 via Groq API)
- 📈 BERT-based ATS Similarity Score
- 🧠 Feedback with section-wise scores (✅, ⚠️, ❌)
- 🔍 Keyword Match and Missing Keywords
- 🔮 Hiring Probability Estimation
- 📥 Downloadable AI Feedback Report
- 🌗 Dark Mode compatible

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Sentence-BERT](https://www.sbert.net/)
- [Groq API](https://console.groq.com/) (for LLaMA-3)
- [PDFMiner](https://github.com/pdfminer/pdfminer.six)
- [Python](https://www.python.org/)

## 📦 Installation

### 1. Clone the repo

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

2. Create Virtual Environment (optional but recommended)
python -m venv myenv
myenv\Scripts\activate  # For Windows
source myenv/bin/activate  # For Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4. Set Environment Variable
Create a .env file in the root folder and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

5. Run the App
streamlit run main.py

📸 Screenshots


🙋‍♂️ Author
Shivam Rajak
🔗 LinkedIn
https://www.linkedin.com/in/shivam-rajak-3177102b8

📄 License
This project is licensed under the MIT License - feel free to use or modify it.
