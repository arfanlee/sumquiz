import streamlit as st
from method_class import sumquiz as sq
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
	st.set_page_config(page_title="SumQuiz", page_icon="📖", layout="wide")
	st.header("📖 SumQuiz App")
	# st.title("Welcome to SumMemory App!")

	st.divider()

	col1, col2 =  st.columns(2, gap="large")
	with col1:
		st.header("About")
		about = "SumMemory allows you it to summarize a file (pdf only) or test your memory with a simple quiz."

		st.write(about)

		st.header("How to use")

		instruction = """

			1. Select which function do you want to use in the sidebar.
			2. Upload a pdf, docx, or txt file📄 (Currently we don't support scanned PDF)
			3. For summary, you can prompt for other query, for example, you can ask the MeryGPT 
			to explain a certain topic like you're a 5 years old.	
			4. For quiz, it would ask a random question from the syllabus, and waiting
			for you to answer.
		"""

		st.markdown(instruction)

	with col2:
		uploaded_file = sq.file_exporter()
		if not uploaded_file:
			st.stop()

		else:
			if uploaded_file is not None:
				if uploaded_file.name.endswith(".pdf"):
					parsed = sq.parse_pdf(uploaded_file)
				else:
					raise ValueError("File type not supported!")

			selected = st.selectbox("Pick one", ["Summary", "Quiz"], index=None, placeholder="Select a function...")

			if selected == "Summary":
				response = sq.summation(client, parsed)
				st.write(response)
				query = st.text_input("Query", placeholder="E.g. Explain further like I'm 5")
				# st.button("Submit")

				if st.button("Submit"):
					sq.summation_ask(client, query, parsed)

			elif selected == "Quiz":
				sq.quiz_show(client, parsed)


if __name__ == "__main__":
    main()