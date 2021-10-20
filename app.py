import streamlit as st
from games import guess_number, guess_word, tic_tac_toe


def init(post_init=False):
    if not post_init:
        st.session_state.pages = {
            'Home': home,
            'Guess Number': guess_number.main,
            'Guess Word': guess_word.main,
            'Tic Tac Toe': tic_tac_toe.main,
        }


def home():

    st.write(
        '''
        # Welcome to My Web App! 👋

        ---

        #### Intro

        I made this web app to finish a project assigned by my professor. 
        While that's the main purpose of why I made this. 
        The real purpose was to improve my coding skill, 
        and I learned a lot while making this web app.
        
        This web app is written purely in Python.
        It contains three games. The games are:

        1. Guess Number
        2. Guess Word
        3. Tic Tac Toe

        All of them can be accessed on the sidebar.
        As for the source code, I will share it when all is finished.
        '''
    )


def draw_style():
    st.set_page_config(
        page_title='fingar-fingar',
        page_icon='🖕'
    )

    style = """
        <style>
            header {visibility: visible;}
            footer {visibility: hidden;}
        </style>
    """

    st.markdown(style, unsafe_allow_html=True)


def cls():
    for key in list(st.session_state.keys()):
        if key != 'pages':
            st.session_state.pop(key)

    init(post_init=True)


def main():
    if 'page' not in st.session_state:
        init()

    draw_style()

    with st.sidebar:
        contact_me, about = st.columns([1.5, .8])
        contact_me.button('✉️ Send me a message')
        about.button('🧑‍💻 ccrsxx')
        page = st.selectbox('Page contents', [
                            'Home', 'Guess Number', 'Guess Word', 'Tic Tac Toe'], on_change=cls)
        if page == 'Home':
            st.image('https://c.tenor.com/-420uI8y-RkAAAAd/anime-welcome.gif', 'moshi-moshi!')

    st.session_state.pages[page]()


if __name__ == '__main__':
    main()
