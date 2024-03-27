import streamlit as st
import re
from io import BytesIO
from pypdf import PdfReader

class sumquiz:
    def file_exporter():
        
        file = st.file_uploader(
            "Upload a pdf file!",
            type=["pdf"],
            help="Scanned documents are not supported yet!")
        
        return file
    
    def parse_pdf(file: BytesIO):
        pdf = PdfReader(file)
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
        
        output_str = ' '.join(output)
        return output_str

    def summation(client, parsed_pdf):
        st.title("Summary")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"system",
                "content": "You're an adept summarizer. You will summarize the text given to a proper reading material for a student."
            },
            {
                "role":"user",
                "content":"""Summarize this: Machine learning is a subfield of artificial intelligence (AI) that focuses on the development of algorithms and 
                statistical models that enable computers to perform tasks without explicit programming. At its core, machine learning is about creating systems 
                that can learn from data, identify patterns, and make decisions or predictions based on that data. It represents a paradigm shift in how we 
                approach problem-solving, shifting from traditional rule-based programming to systems that can learn and adapt from experience. The roots of 
                machine learning can be traced back to the early days of computing, but it has gained significant traction and prominence in recent decades, 
                fueled by advancements in computational power, the availability of large datasets, and innovations in algorithmic techniques. Today, machine 
                learning is driving transformative change across a wide range of industries and applications, from finance and healthcare to transportation and 
                entertainment."""
            },
            {
                "role":"assistant",
                "content":"""Machine learning, a branch of AI, enables computers to perform tasks without explicit programming by developing algorithms and models 
                that learn from data to make predictions or decisions. It marks a shift from rule-based programming to systems that learn from experience. Dating 
                back to early computing, it has surged in recent years due to advancements in computation, data availability, and algorithms. Today, it drives 
                innovation across industries like finance, healthcare, and entertainment."""
            },
            {
                "role":"user",
                "content": parsed_pdf
            }],
            max_tokens=400,
            temperature=1.3
        )

        parsed_content = response.choices[0].message.content
        return parsed_content
        
    def summation_ask(client, query, content):
        response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"system",
            "content": "You're a excellent responder. You will answer the query with the provided info in the sentence."
        },
        {
            "role":"user",
            "content":"""What is the root of machine learning according to this sentence?: Machine learning is a subfield of artificial intelligence (AI) 
            that focuses on the development of algorithms and  statistical models that enable computers to perform tasks without explicit programming. At 
            its core, machine learning is about creating systems  that can learn from data, identify patterns, and make decisions or predictions based on 
            that data. It represents a paradigm shift in how we  approach problem-solving, shifting from traditional rule-based programming to systems that 
            can learn and adapt from experience. The roots of  machine learning can be traced back to the early days of computing, but it has gained significant 
            traction and prominence in recent decades, fueled by advancements in computational power, the availability of large datasets, and innovations in
            algorithmic techniques. Today, machine learning is driving transformative change across a wide range of industries and applications, from finance
            and healthcare to transportation and entertainment."""
        },
        {
            "role":"assistant",
            "content":"""The origins of machine learning can be linked to the initial stages of computing, yet its notable rise to prominence has occurred more 
            recently, driven by advancements in computational capabilities, the accessibility of vast datasets, and breakthroughs in algorithmic methodologies."""
        },
        {
            "role":"user",
            "content":f"Answer this question: '{query}'' based on the content '{content}'"
        }]
        )

        query_answered = response.choices[0].message.content
        return query_answered