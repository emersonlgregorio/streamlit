import streamlit as st
from common.tags import Tag
from streamlit_superapp import State

# def access_denied():
#     if st.session_state['role'] == "admin":
#         main()
#     else:
#         st.error("You don't have access to this page.")

# print('*******************************')
# print(st.session_state['role'])
# print('*******************************')

# def _access_denied():
#     if st.session_state['role'] == "admin":
#         main()
#     else:
#         st.error("You don't have access to this page.")


NAME = "Counter"
ICON = "🔢"
# ACCESS = _access_denied()




def main(page):
    counter = State("counter", default_value=0, key=page)

    if st.button("Increment"):
        counter.value += 1

    st.write(f"counter: {counter.value}")

    st.code(
        """
import streamlit as st
from common.tags import Tag
from streamlit_superapp import State


NAME = "Counter"
TAG = Tag.DEMO
ICON = "🔢"


def main(page):
    counter = State("counter", default_value=0, key=page)

    if st.button("Increment"):
        counter.value += 1

    st.write(f"counter: {counter.value}")
    """
    )
