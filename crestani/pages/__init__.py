import streamlit as st

NAME = "Pages"
ICON = "🔢"

st.session_state["page_loader_paths"] = [item for item in st.session_state["page_loader_paths"] if "compras" not in item]

st.write(st.session_state)

# for page in st.session_state['page_loader_paths']:
#     if 'compras' in page:
#         del