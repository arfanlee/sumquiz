import streamlit as st

st.title("Quiz Time!")

def clear_submit():
    st.session_state["submit"] = False

file = st.file_uploader(
    "Upload a .pdf, .docx or .txt file.",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
    on_change=clear_submit)

words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna?"""

for word in words:
    st.write_stream(word)

# st.text_input("Answer")
query = st.text_area("Ask a question about the document.")

st.button("Submit")