import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai


from pdf import extract_text  # method in pdf.py file
key = os.getenv("Google_API_KEY")

genai.configure(api_key=key)

# Change this line:
model = genai.GenerativeModel('gemini-2.5-flash-lite')  # Use the correct model name for Gemini 2.5 Flash Lite

def analyze_resume(pdf_doc, job_des):
    
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write(f'Text Extracted Successfully from the PDF document.')
        
    else:
        st.warning('Error !! Drop the file in pdf format!!')
        
    ats_score = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the ATS score
                                       out of 100 and also give me the feedback on how to improve the resume 
                                       to get a better score.
                                       
                                       Generate the results in bullet points
                                       (maximum 5 points)''')
    
    probability = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the probability of 
                                       getting short listed for thje given job description in percentage.
                                       
                                        Generate the results in bullet points
                                       (maximum 5 points)''')
    
    good_fit = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the feedback on how good fit the
                                       candidate.
                                       
                                       
                                       Generate the results in bullet points
                                       (maximum 5 points)''')
    
    skill_match = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the feedback on how good the 
                                       skill match is between the resume and job description.
                                       
                                         Generate the results in bullet points
                                        (maximum 5 points)''')
    
    missing_keywords = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the feedback on what are the missing keywords
                                       in the resume that are present in the job description.
                                       
                                         Generate the results in bullet points
                                       (maximum 5 points)''')

    swot = model.generate_content(f''' Compare the given pdf {pdf_text} and
                                       given job description {job_des} and give me the feedback on what are the strengths,
                                       weaknesses, opportunities and threats in the resume with respect to the job description.
                                       
                                        Generate the results in bullet points
                                       (maximum 5 points)''')
    
    return st.write(f'''ATS Score: {ats_score.text}
                          Probability of getting shortlisted: {probability.text}
                          Good Fit: {good_fit.text}
                          Skill Match: {skill_match.text}
                          Missing Keywords: {missing_keywords.text}
                          SWOT Analysis: {swot.text}''')