import streamlit as st

if 'shit' not in st.session_state:
    st.session_state.shit = 0

def cls():
    st.session_state.shit +=1

guess = st.number_input('Ask something bruh', key=st.session_state.shit, min_value=0, max_value=100)

st.button('fuck me here', on_click=cls)

st.write(st.session_state)
st.write(guess)