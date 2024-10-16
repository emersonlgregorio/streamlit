import streamlit as st
from utils.menu import menu
from streamlit_card import card

menu()

# Here goes your normal streamlit app
st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
option = st.selectbox('NLP Service', ('Sentiment Analysis', 'Entity Extraction', 'Text Summarization'))
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(height=150):
        st.selectbox('Select your option', ['Option 1', 'Option 2', 'Option 3'])

with col2:
    with st.container(height=150):
        st.selectbox('Select option', ['Option 1', 'Option 2', 'Option 3'])

with col3:
    with st.container(height=150):
        if st.button("Clique aqui!", key="card_button"):
            st.write("Você clicou no card!")

