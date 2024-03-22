import streamlit as st
from method_class import sumquiz as sq

st.title("Welcome to SumMemory App!")

st.divider()

st.header("About")
about = "SumMemory allows you to ask questions about your documents and get accurate answers with instant citations.  You can use it to summarize a paper or test you memory with quizzes."

st.write(about)

st.header("How to use")

instruction = """

    - Select which function do you want to use in the sidebar.
    - Upload a pdf, docx, or txt file📄 (Currently we don't support scanned PDF)
    - For summary, you can prompt for other query, for example, you can ask the MeryGPT 
      to explain a certain topic like you're a 5 years old.
    - For quiz, it would ask a random question from the syllabus, and waiting
      for you to answer.
"""

st.markdown(instruction)

selected = st.selectbox("Pick one", ["Summary", "Quiz"], index=None, placeholder="Select a function...")

if selected == "Summary":
    sq.summation_show()

elif selected == "Quiz":
    sq.quiz_show()