import streamlit as st
from method_class import sumquiz as sq
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
	st.set_page_config(page_title="SumGPT", page_icon="📖", layout="wide")
	st.header("📖 SumGPT App")
	# st.title("Welcome to SumMemory App!")

	st.divider()

	col1, col2 = st.columns(2, gap="large")
	with col1:
		st.header("About")
		about = "SumGPT allows you it to summarize a file (pdf only) and ask it anything about the document."

		st.write(about)

		st.header("How to use")

		instruction = """

			2. Upload a pdf file📄 (Currently we don't support scanned PDF)
			3. For summary, you can prompt for other query, for example, you can ask the SumGPT 
			to explain a certain topic like you're a 5 years old.
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

			response = sq.summation(client, parsed)
			st.write(response)
			query = st.text_input("Query", placeholder="E.g. Explain further like I'm 5")

			if st.button("Submit"):
				query_answered = sq.summation_ask(client, query, parsed)
				st.header("Answer")
				st.write(query_answered)


if __name__ == "__main__":
    main()