import streamlit as st
# from streamlit_modal import Modal
from modal_streamlit_vmateo import Modal

modal = Modal(
    title="Demo Modal", 
    key="demo-modal",
    padding=20,    # default value
    max_width=1200,  # default value
)


nota_id = st.button("Abrir Modal")

st.write(nota_id)

if nota_id:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")
        btn_fechar = st.button("Fechar Modal")
        if btn_fechar:
            modal.close()
        