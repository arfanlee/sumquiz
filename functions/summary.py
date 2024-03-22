import streamlit as st

st.title("Summary")

file = st.file_uploader("Upload a .pdf, .docx or .txt file.")

st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
         Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt. Blandit turpis cursus in hac habitasse platea. Nulla
          pellentesque dignissim enim sit amet venenatis. Enim nunc faucibus a pellentesque sit amet porttitor eget. Pulvinar elementum i
         nteger enim neque volutpat ac tincidunt. Nibh ipsum consequat nisl vel pretium lectus quam id leo. Sed libero enim sed faucibus 
         turpis in. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Pulvinar mattis nunc sed blandit libero """)

st.text_input("Query", placeholder="E.g. Explain further like I'm 5")

st.button("Submit")