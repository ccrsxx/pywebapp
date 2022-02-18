import streamlit as st


def main():
    st.markdown(
        '''
        <h1 align="center">
            Welcome to My Web App 👋
        </h1>

        ---

        #### About

        I made this web app to finish a project assigned by my teacher. 
        While that's the main purpose of why I made this. 
        The real purpose was to improve my coding skill, 
        and I learned a lot while making this web app.
        
        This web app is written entirely in Python.
        It contains three games. The games are:

        1. Guess Number
        2. Guess Word
        3. Tic Tac Toe

        All of them can be accessed on the sidebar.
        As for the source code, you can find it on the source tab.
        ''',
        unsafe_allow_html=True,
    )


if __name__ == '__main__':
    main()
