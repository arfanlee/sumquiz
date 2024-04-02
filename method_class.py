import re
from io import BytesIO
from pypdf import PdfReader

class DoChat:
    def parse_pdf(parsed_file: BytesIO):
        pdf = PdfReader(parsed_file)
        output = []
        for page in pdf.pages:
            text = page.extract_text()
            # Merge hyphenated words
            text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
            # Fix newlines in the middle of sentences
            text = re.sub(r"(?<!\n\s)\n(?!\s\n)", " ", text.strip())
            # Remove multiple newlines
            text = re.sub(r"\n\s*\n", "\n\n", text)
            # Remove unicode characters
            text = re.sub(r'[^\x00-\x7F]+', '', text)

            output.append(text)
        
        return ' '.join(output)

    def chat_doc(client, query, parsed_file):
        response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"system",
            "content": "You're a excellent teacher. You will answer the query with the provided info in the sentence."
        },
        {
            "role":"user",
            "content":f"Answer this question: '{query}' based on the content '{parsed_file}'"
        }]
        )

        query_answered = response.choices[0].message.content
        return query_answered