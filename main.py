import streamlit as st
from method_class import DoChat as dc
from openai import OpenAI

client = OpenAI(
	api_key=st.secrets["OPENAI_API_KEY"]
)

def main():
	st.set_page_config(page_title="AskDoc", page_icon="💬")
	st.header("💬 AskDoc")

	st.write("""
		Tired of sifting through documents? AskDoc is your friendly AI assistant that helps you chat with your files!
		Ask questions, get key insights and summaries, and explore the content of your documents in a whole new way.""")

	uploaded_file = st.file_uploader(
		"Choose a file",
		type=["pdf"],
		help="Scanned documents are not supported yet!")

	if not uploaded_file:
		st.stop()

	else:
		if uploaded_file.name.endswith(".pdf"):
			parsed_file = dc.parse_pdf(uploaded_file)
		else:
			raise ValueError("File type not supported!")

		if "messages" not in st.session_state:
			st.session_state.messages = [
			{
				"role":"assistant",
				"content":"How can I help you?"
			}
		]
		
		# Display chat messages from history on app rerun
		for message in st.session_state.messages:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])
		
		# Accept user input
		query = st.chat_input("Ask me anything about the document.")

		if query:
		# Append new messages to history
		# Displaying the User Message
			with st.chat_message("user"):
				st.markdown(query)

			response = dc.chat_doc(client, query, parsed_file)
			with st.chat_message("ai"):
				st.markdown(response)

			st.session_state.messages.append(
				{
					"role": "user",
					"content": query
				}
			)

			st.session_state.messages.append(
				{
					"role": "assistant",
					"content": response
				}
			)

if __name__ == "__main__":
    main()