import streamlit as st
from games import TicTacToe


def page():
    style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def main():
    page()
    TicTacToe.play()


if __name__ == '__main__':
    main()
