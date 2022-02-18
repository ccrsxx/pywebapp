import streamlit as st
import smtplib
import time
import os


def send_mail(sender: str, body: str):
    if any(content == '' for content in (sender, body)):
        placeholder.warning('Either sender or message is missing. Try again.')
        return time.sleep(2)

    email = os.getenv('email')
    password = os.getenv('password')
    target = os.getenv('target')

    if email is None:
        email = st.secrets['email']
        password = st.secrets['password']
        target = st.secrets['target']

    cls()

    with placeholder.progress(0):
        time.sleep(1)
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        placeholder.progress(10)
        conn.ehlo()
        placeholder.progress(20)
        conn.starttls()
        placeholder.progress(40)
        conn.login(email, password)
        placeholder.progress(60)
        conn.sendmail(email, target, f'Subject: From {sender}\n\n{body}')
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
        <h1 align="center">
            Send me a message
        </h1>

        ---
        ''',
        unsafe_allow_html=True,
    )

    if 'input' not in st.session_state:
        st.session_state.input = 0

    sender = st.text_input('Sender', value='Anonymous')
    text = st.text_area('Message', key=st.session_state.input)
    st.button('Send', on_click=send_mail, args=(sender, text))


if __name__ == '__main__':
    main()
