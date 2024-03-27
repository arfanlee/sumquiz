import streamlit as st
import re
from io import BytesIO
from pypdf import PdfReader
import ast

class sumquiz:
    def file_exporter():
        
        file = st.file_uploader(
            "Upload a pdf file!",
            type=["pdf"],
            help="Scanned documents are not supported yet!")
        
        return file

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

        st.write(parsed_content)
        
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

        st.header("Answer")
        st.write(query_answered)

    def quiz_show(client, content):
        st.title("Quiz Time!")

        response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"system",
            "content": "You're a excellent quizzer. You will ask the user with the provided info in the sentence."
        },
        {
            "role":"user",
            "content":"""Ask a quick quiz from this information and an answer to it in a Python list, ['Question', 'Answer'] e.g. '['What is AI', 'AI stands for Artificial Intelligence']': 
            Artificial intelligence is a rapidly evolving field in computer science that explores the creation of intelligent machines capable of mimicking human 
            cognitive functions, including learning, problem-solving, and decision-making."""
        },
        {
            "role":"assistant",
            "content":"['In which industries can machine learning be used in?', 'Machine learning can applied in finance and healthcare to transportation and entertainment.']"
        },
        {
            "role":"user",
            "content":f"Create a a question based on this information '{content}'"
        }]
        )

        question = response.choices[0].message.content
        question = ast.literal_eval(question)
        ask = question[0]
        ai_answer = question[1]
        print(ai_answer)
        # print(type(ai_answer))

        st.header("Question")
        st.write(ask)
        with st.form(key="qa_form"):
            user_answer = st.text_area("Answer the question")
            submit = st.form_submit_button("Submit")

        if submit:
            st.write(compare_answer(client, ai_answer, user_answer))
    
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
    
def compare_answer(client, ai_answer, user_answer):
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"system",
            "content": "You're a excellent teacher. You will compare the answer from user with the correct answer."
        },
        {
            "role":"user",
            "content":"""Does the answer: AI stands for Artificial Imagination. Equivalent with correct answer: AI stands for Artificial Intelligence."""
        },
        {
            "role":"assistant",
            "content":"Wrong. AI stands for Artificial Intelligence not Artificial Imagination.."
        },
        {
            "role":"user",
            "content":"""Does the answer: AI stands for Artificial Intelligence. Equivalent with correct answer: AI stands for Artificial Intelligence."""
        },
        {
            "role":"assistant",
            "content":"Correct. AI is indeed stands for Artificial Intelligence."
        },
        {
            "role":"user",
            "content":f"Is the answer: {user_answer} equivalent with the correct answer {ai_answer}"
        }]
        )
    compared_answer = response.choices[0].message.content
    return compared_answer