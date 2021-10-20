import streamlit as st
import random
import json
import os


def get_word(language: str, length: int) -> str:
    with open(os.path.abspath(os.path.join('assets', 'language.json'))) as raw:
        data = json.load(raw)[language]
        word = random.choice(data)

        while not 3 <= len(word) <= length or any(c in word for c in [' ', '-']):
            word = random.choice(data)

        return word


def init(language: str = 'English', length: int = 6, heart: int = 5, post_init=False):
    if not post_init:
        st.session_state.input = 0
        st.session_state.win = 0
    st.session_state.word = get_word(language, length)
    st.session_state.lives = heart
    st.session_state.guessed = []


def restart():
    init(st.session_state.language, st.session_state.length,
         st.session_state.heart, post_init=True)
    st.session_state.input += 1


def main():
    if 'word' not in st.session_state:
        init()

    st.title('🔠 Guess Word')
    st.write('University project, still in development by **ccrsxx#8408**')

    reset, win, lives, settings = st.columns([.45, .3,  1, 1])
    reset.button('New game', on_click=restart)

    with settings.expander('Settings'):
        st.write('**Warning**: changing one of these settings will restart your game')
        st.selectbox('Set language', [
                     'English', 'Indonesia'], key='language', on_change=restart)
        st.select_slider('Set hearts', list(range(1, 11)),
                         5, key='heart', on_change=restart)
        st.slider('Set length of the word', 3, 20,
                  6, key='length', on_change=restart)

    placeholder, debug = st.empty(), st.empty()
    guess = placeholder.text_input(
        'Guess a letter', key=st.session_state.input, max_chars=1).lower()

    if not guess or not guess.isalpha():
        debug.write('Please input letter')
    elif guess in st.session_state.guessed:
        debug.warning(f"You already guessed **{guess}**")
    elif guess not in st.session_state.word:
        debug.warning(f"The word has no **{guess}**")
        st.session_state.lives -= 1
        st.session_state.guessed.append(guess)
    else:
        debug.info('Good guess')
        st.session_state.guessed.append(guess)

    if st.session_state.lives == 0:
        debug.error(
            f"😓 **You lost**, the word was **{st.session_state.word}**")
        placeholder.empty()
    elif all(c in st.session_state.guessed for c in st.session_state.word):
        debug.success(f"🎈 **YOU WIN**")
        st.session_state.win += 1
        placeholder.empty()

    lives.button(
        f'{("❤️" * st.session_state.lives) if st.session_state.lives else "💀 Lost"}')
    win.button(f'🏆 {st.session_state.win}')

    guess_box, letter_box = st.columns([1, .23])

    guess_box.button(
        ' - '.join([c if c in st.session_state.guessed else '_' for c in st.session_state.word]))
    letter_box.button(
        f'{" ".join(st.session_state.guessed) if st.session_state.guessed else "Letter History"}')


if __name__ == '__main__':
    main()
