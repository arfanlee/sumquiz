import streamlit as st

st.title("Welcome to SumMemory App!")

st.divider()

st.header("About")
about = "SumMemory allows you to ask questions about your documents and get accurate answers with instant citations.  You can use it to summarize a paper or test you memory with quizzes."

st.write(about)

st.header("How to use")

how_use = """

    - Select which function do you want to use in the sidebar.
    - Upload a pdf, docx, or txt file📄 (Currently we don't support scanned PDF)
    - For summary, you can prompt for other query, for example, you can ask the MeryGPT 
      to explain a certain topic like you're a 5 years old.
    - For quiz, it would ask a random question from the syllabus, and waiting
      for you to answer.
"""

st.markdown(how_use)

selected = st.selectbox("Pick one", ["Summary", "Quiz"], index=None, placeholder="Select a function...")

if selected == "Summary":
    st.title("Summary")

    file = st.file_uploader("Upload a .pdf, .docx or .txt file.")

    st.write("""Lorem ipsum dolor sit amet, libero """)

    st.text_area("Query", placeholder="E.g. Explain further like I'm 5")

    st.button("Submit")

elif selected == "Quiz":
    st.title("Quiz")
    file = st.file_uploader(
    "Upload a .pdf, .docx or .txt file.",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!")

    words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna?"""

    st.write(words)

    st.text_input("Answer")

    st.button("Submit")