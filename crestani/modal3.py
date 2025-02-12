import streamlit as st
from streamlit_modal import Modal

modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=1200  # default value
)

open_modal = st.button("Open")

if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

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