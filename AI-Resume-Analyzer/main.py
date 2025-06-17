import streamlit as st
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
import re
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from datetime import datetime
import time

# Load environment variables
dotenv_path = ".env"
load_dotenv(dotenv_path)
api_key = os.getenv("GROQ_API_KEY")

# Session State Defaults
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
if "resume" not in st.session_state:
    st.session_state.resume = ""
if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""

# Set Page Config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

# App Header
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🧠 AI Resume Analyzer</h1>
    <h4 style='text-align: center; color: gray;'>by Shivam Rajak</h4>
    <hr style='border: 1px solid #ddd;'/>
""", unsafe_allow_html=True)

# Extract text from PDF
def extract_pdf_text(uploaded_file):
    try:
        return extract_text(uploaded_file)
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

# BERT Similarity
def calculate_similarity_bert(text1, text2):
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    return cosine_similarity(emb1, emb2)[0][0]

# Keyword Extractor
def extract_keywords(text):
    return set(re.findall(r'\b\w+\b', text.lower()))

# Get AI Feedback
def get_report(resume, job_desc):
    client = Groq(api_key=api_key)
    prompt = f"""
    You are an AI Resume Analyzer. Analyze the following resume against the job description.
    Evaluate all relevant skills, experience, and alignment.
    Score each section out of 5 with an emoji (✅, ❌, ⚠️) and explanation.

    - Start each evaluation point with this exact format: Score: x/5 followed by emoji and explanation. (Example: "Score: 4/5 ✅ Explanation...")

    End with: Suggestions to improve your resume.

    Resume:
    {resume}

    Job Description:
    {job_desc}
    """
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Extract Scores from AI Report
def extract_scores(text):
    pattern = r'Score:\s*(\d+(?:\.\d+)?)/5'
    matches = re.findall(pattern, text)
    return [float(score) for score in matches]

# Input Form
if not st.session_state.form_submitted:
    with st.form("my_form"):
        resume_file = st.file_uploader("📄 Upload Resume (PDF only)", type="pdf")
        st.session_state.job_desc = st.text_area("💼 Paste Job Description", height=250)
        submitted = st.form_submit_button("🚀 Analyze Resume")
        if submitted:
            if resume_file and st.session_state.job_desc:
                st.session_state.resume = extract_pdf_text(resume_file)
                st.session_state.form_submitted = True
                st.rerun()
            else:
                st.warning("Please upload resume and paste job description.")

# Output
if st.session_state.form_submitted:
    with st.spinner("🔎 Generating ATS score and AI feedback..."):
       

        ats_score = calculate_similarity_bert(st.session_state.resume, st.session_state.job_desc)
        report = get_report(st.session_state.resume, st.session_state.job_desc)
        scores = extract_scores(report)
        avg_score = round(sum(scores) / (5 * len(scores)), 2) if scores else 0.0

        # Keywords Match
        jd_keywords = extract_keywords(st.session_state.job_desc)
        resume_keywords = extract_keywords(st.session_state.resume)
        matched = jd_keywords & resume_keywords
        missing = jd_keywords - resume_keywords

    col1, col2 = st.columns(2)
    with col1:
        st.metric("📈 ATS Similarity Score", f"{ats_score:.2f}")
    with col2:
        st.metric("🤖 AI Evaluation Score", f"{avg_score:.2f} / 1.00")

    st.markdown(f"""
    <div style='text-align: left; background-color: #000000; color: #ffffff; padding: 15px; border-radius: 10px; margin: 10px 0; font-family: monospace; font-size: 16px; line-height: 1.6;'>
        {report}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Keywords Match Analysis")
    st.success(f"✅ Matched Keywords: {', '.join(sorted(matched))}")
    st.error(f"❌ Missing Keywords: {', '.join(sorted(missing))}")

   
    # Hiring Probability
    st.markdown("### 🔮 Hiring Probability")
    if avg_score >= 0.7:
        st.success("🎯 High probability of shortlisting!")
    elif avg_score >= 0.4:
        st.warning("🟡 Medium probability. Try improving the missing parts!")
    else:
        st.error("🔴 Low probability. Resume needs significant improvement.")

    st.download_button("📥 Download Report", report, file_name="AI_Resume_Report.txt")

    st.caption(f"🕒 Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size: 14px;'>
    Made with ❤️ by <a href='https://www.linkedin.com/in/shivam-rajak-3177102b8' target='_blank'>Shivam Rajak</a>
</p>
""", unsafe_allow_html=True)