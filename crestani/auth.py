import streamlit as st
import app

st.session_state['authenticated'] = True
st.session_state['username'] = 'Admin'
st.session_state['role'] = 'admin'

if st.session_state['authenticated']:
    # st.write('Welcome, ' + st.session_state['username'] + '!')
    app.main()