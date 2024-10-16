import streamlit_superapp
from streamlit_superapp import State
import streamlit as st

st.set_page_config(page_title="Streamlit Super App", page_icon="🚀", layout="wide")

# authenticated = State("authenticated", default_value=False)
# username = State("username", default_value="Admin")
# role = State("role", default_value="admin",key=pageu)
# role.bind('admin')

# st.session_state['authenticated'] = True
# st.session_state['username'] = 'Admin'
# st.session_state['role'] = 'admin'

# authenticated.bind()


streamlit_superapp.run()
