import streamlit as st
from games import tictactoe


def page():
    st.set_page_config(
        page_title='rip brain',
        page_icon='🪦'
    )

    style = """
        <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """

    st.markdown(style, unsafe_allow_html=True)


def main():
    page()
    tictactoe.main()


if __name__ == '__main__':
    main()
