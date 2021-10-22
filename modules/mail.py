import streamlit as st
import smtplib
import time
import os


def send_mail(body: str, email: str = os.getenv('email'), password: str = os.getenv('password')):
    cls()

    with placeholder.progress(0):
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        placeholder.progress(10)
        conn.ehlo()
        placeholder.progress(20)
        conn.starttls()
        placeholder.progress(40)
        conn.login(email, password)
        placeholder.progress(60)
        conn.sendmail(email, 'aminrisal@gmail.com', f'Subject: From WebApp\n\n{body}')
        placeholder.progress(80)
        conn.quit()
        placeholder.progress(100)
        time.sleep(1)


    placeholder.success('Success. I will take a look at your message, thanks!')
    time.sleep(3)
    placeholder.empty()


def cls():
    st.session_state.input += 1


def main():
    global placeholder
    placeholder = st.empty()

    placeholder.markdown(
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
