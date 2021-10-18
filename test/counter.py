import random
import streamlit as st

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.game = 0
    st.session_state.tries = 0
    st.session_state.max = 100
    st.session_state.win = False


def change_range():
    st.session_state.number = random.randint(1, st.session_state.max)


st.title('🔢 Guess Number')

reset, won_game, set_range = st.columns([.4, 1, 1])

if reset.button('New game'):
    st.session_state.number = random.randint(1, st.session_state.max)
    st.session_state.tries = 0
    st.session_state.win = False

won_game.button(f'🏆 {st.session_state.game}')

with set_range.expander('Set range'):
    st.number_input('Input max range, Default=100', min_value=1,
                    key='max', on_change=change_range)

if not st.session_state.win:
    guess = st.number_input(
        f'Enter your guess from 1 - {st.session_state.max}', min_value=0, max_value=st.session_state.max)

    if guess:
        st.session_state.tries += 1
        if guess < st.session_state.number:
            st.warning(f'{guess} is too low!')
        elif guess > st.session_state.number:
            st.warning(f'{guess} is too high!')
        else:
            st.success(
                f'🎈 Yay! you guessed it right, it only took you {st.session_state.tries} tries')
            st.session_state.win = True
            st.session_state.game += 1
