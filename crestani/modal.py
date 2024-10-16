import streamlit as st
from streamlit_modal import Modal

def show_modal(open_modal):
    modal = Modal(
        "Demo Modal", 
        key="demo-modal",
    
        # Optional
        padding=20,    # default value
        max_width=1200  # default value
    )

    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("Text goes here")


st.write('Teste Modal')
open_modal = st.button("Open")
st.write(open_modal)
if open_modal:
    st.write('Botão clicado')
    show_modal(open_modal)  
else:
    st.write('Não clicado')
# st.write(open_modal)




        # html_string = '''
        # <h1>HTML string in RED</h1>

        # <script language="javascript">
        #   document.querySelector("h1").style.color = "red";
        # </script>
        # '''
        # components.html(html_string)

        # st.write("Some fancy text")
        # value = st.checkbox("Check me")
        # st.write(f"Checkbox checked: {value}")