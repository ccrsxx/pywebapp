import streamlit as st


def main():
    st.markdown(
        '''
        ## Source Code
        
        Finally It's finished. Now, you can find the source code [here](https://github.com/ccrsxx/University-Project) on my Github repository.

        ## Contributing to My Project

        I love your input! You can contribute to the project with:

        - Reporting a bug
        - Discussing the current state of the code
        - Submitting a fix
        - Proposing new features
        - Becoming a maintainer

        ## License

        By contributing, you agree that your contributions will be licensed under its MIT License.
        ''', 
        unsafe_allow_html=True)


if __name__ == '__main__':
    main()
