import streamlit as st

from pdf import extract_text
from analysis import analyze_resume # Method in analysis.py file

st.set_page_config(page_title="Resume Analyzer", page_icon='🛠️', layout="centered")

st.title("Resume Analyzer Using AI 🤖🧠 ")

st.header(':blue[AI Powered resume Analyzer with given Job Description📋🤖]')

st.subheader(''' This page helps you to compare the resume and given job description and provide ATS Score, probability of getting shortlisted, skill match, good fit and also give you the feedback on how to improve your resume to get a better score📌.''')

st.sidebar.subheader('Drop your resume here 👇')

pdf_doc = st.sidebar.file_uploader('Click Here', type=['pdf'])

st.sidebar.markdown('Designed by Ashok S')
st.sidebar.markdown('Git Hub : https://github.com/ashoks06607-hub/resume_analyzer.ai.git')

job_des = st.text_area('Copy and paste the Job Description Here 👇', max_chars= 10000)

submit = st.button('Get The Results📊')

if submit:
    with st.spinner('Loading...⌛'):
      analyze_resume(pdf_doc, job_des)
      
