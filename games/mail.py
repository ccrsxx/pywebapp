import streamlit as st
import smtplib
import os


def send_mail(body: str):
    cls()

    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(os.getenv('email'), os.getenv('password'))
    conn.sendmail(os.getenv('email'), os.getenv(
        'email'), f'Subject: From WebApp\n\n{body}')
    conn.quit()

    st.success('Success. I will take a look at your message, thanks!')


def cls():
    st.session_state.input += 1


def main():
    st.image('https://c.tenor.com/xTB4BrdufJMAAAAC/anime-emilia.gif', 'Emilia', 400)
    if 'input' not in st.session_state:
        st.session_state.input = 0

    text = st.text_area('Sent me a message', key=st.session_state.input)
    st.button('Send', on_click=send_mail, args=(text, ))


if __name__ == '__main__':
    main()
