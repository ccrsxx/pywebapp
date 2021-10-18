import streamlit as st

if 'first' not in st.session_state:
    st.session_state.first = ''

def update_first():
    st.session_state.first = ''


st.title('🪞 Mirrored Widgets using Session State')

st.text_input(label='Textbox 1', key='first',
 on_change=update_first, value=st.session_state.first)