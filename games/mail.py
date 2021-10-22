import streamlit as st
import smtplib
import os


def send_mail(body: str, email: str = os.getenv('email'), password: str = os.getenv('password')):
    cls()

    st.success(f'{email}, {password}')

    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(email, password)
    conn.sendmail(email, email, f'Subject: From WebApp\n\n{body}')
    conn.quit()

    st.success('Success. I will take a look at your message, thanks!')


def cls():
    st.session_state.input += 1


def main():
    st.markdown(
        '''
        # Say something nice please...
        
        ---

        <p align="center">
            <img width="400" height="250" src="https://c.tenor.com/Y9g7q5u4W8IAAAAC/girl-please.gif" alt="preasee.."/>
        </p>
        '''
    , unsafe_allow_html=True)

    if 'input' not in st.session_state:
        st.session_state.input = 0

    text = st.text_area('Sent me a message', key=st.session_state.input)
    st.button('Send', on_click=send_mail, args=(text, ))


if __name__ == '__main__':
    main()
