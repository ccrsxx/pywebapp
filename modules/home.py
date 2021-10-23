import streamlit as st


def main():
    st.markdown(
        '''
        <h1 align="center">
            Welcome to my Web App ~ <img src="https://user-images.githubusercontent.com/1303154/88677602-1635ba80-d120-11ea-84d8-d263ba5fc3c0.gif" width="50px" alt="wave">
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
        As for the source code, I will share it once all is finished.
        '''
    , unsafe_allow_html=True)


if __name__ == '__main__':
    main()
