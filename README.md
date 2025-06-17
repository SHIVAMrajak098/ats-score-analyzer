🧠 AI Resume Analyzer
Analyze your resume against job descriptions using AI & BERT. Get similarity scores, keyword insights, and personalized suggestions.

   

🚀 Features
📄 Upload Resume (PDF)
💼 Paste Job Description
🤖 Get AI-Powered Feedback using Groq (LLaMA 3)
📈 BERT-based ATS Score (semantic similarity)
📌 Keyword Match – see what’s missing!
🔮 Hiring Probability estimate
📥 Downloadable full report
🧠 Built with Streamlit, sentence-transformers, and Groq LLM

⚙️ Installation
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


## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Sentence-BERT](https://www.sbert.net/)
- [Groq API](https://console.groq.com/) (for LLaMA-3)
- [PDFMiner](https://github.com/pdfminer/pdfminer.six)
- [Python](https://www.python.org/)



🙋‍♂️ Author
Shivam Rajak
🔗 LinkedIn
https://www.linkedin.com/in/shivam-rajak-3177102b8

📄 License
This project is licensed under the MIT License - feel free to use or modify it.
