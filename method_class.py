import streamlit as st

class sumquiz:
    def file_exporter():
        
        file = st.file_uploader(
            "Upload a .pdf, .docx or .txt file.",
            type=["pdf", "docx", "txt"],
            help="Scanned documents are not supported yet!")
        
        return file

    def summation_show():
        st.title("Summary")

        st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt. Blandit turpis cursus in hac habitasse platea. Nulla
                pellentesque dignissim enim sit amet venenatis. Enim nunc faucibus a pellentesque sit amet porttitor eget. Pulvinar elementum i
                nteger enim neque volutpat ac tincidunt. Nibh ipsum consequat nisl vel pretium lectus quam id leo. Sed libero enim sed faucibus 
                turpis in. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Pulvinar mattis nunc sed blandit libero """)

        st.text_input("Query", placeholder="E.g. Explain further like I'm 5")

        st.button("Submit")

    def quiz_show():
        st.title("Quiz Time!")

        vector_index = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna?"""

        st.write(vector_index)

        # st.text_input("Answer")
        query = st.text_area("Ask a question about the document.")

        st.button("Submit")