import os
import streamlit as st
from games import guess_word


def page():
    st.set_page_config(
        page_title='Guess Word',
        page_icon='🔠'
    )

    style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def main():
    os.environ['DISPLAY'] = ':0'
    page()
    guess_word.main()


if __name__ == '__main__':
    main()
