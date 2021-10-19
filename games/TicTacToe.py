import streamlit as st
import numpy as np
import random


def init(post_init=False):
    if not post_init:
        st.session_state.opponent = 'Computer'
        st.session_state.win = {'X': 0, 'O': 0}
    st.session_state.board = np.full((3, 3), '.', dtype=str)
    st.session_state.player = 'X'
    st.session_state.mutate = True
    st.session_state.winner = None

def check_state():
    if st.session_state.winner and st.session_state.mutate:
        st.session_state.mutate = False
        st.session_state.win[st.session_state.winner] = st.session_state.win.get(st.session_state.winner, 0) + 1
        st.success(f"Congrats! {st.session_state.winner} won the game! 🎈")
    elif not board_available() and not st.session_state.winner:
        st.info(f'Tie')


def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None


def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return None


def check_win(board):
    # transposition to check rows, then columns
    for new_board in [board, np.transpose(board)]:
        result = check_rows(new_board)
        if result:
            return result
    return check_diagonals(board)


def board_available(extra=False):
    raw_moves = [row for col in st.session_state.board.tolist() for row in col]
    available_moves = [i for i, spot in enumerate(raw_moves) if spot == '.']
    if extra:
        return [(i // 3, i % 3) for i in available_moves]
    return available_moves


def computer_player():
    moves = board_available(True)
    if moves:
        c_move = random.choice(moves)
        handle_click(c_move[0], c_move[1])

def play():
    global handle_click
    st.write("""
        # 🕹️ Tic Tac Toe
        in development now for university... by **ccrsxx#8408**
    """)

    # Initialize state.
    if "board" not in st.session_state:
        init()

    reset, score, player, settings = st.columns([.5, .6,  1, 1])
    reset.button('New game', on_click=init, args=(True, ))

    with settings.expander('Settings'):
        st.write('**Warning**: changing one of these settings will restart your game')
        st.selectbox('Set opponent', ['Computer', 'Human'], key='opponent', on_change=init, args=(True, ))

    # Define callbacks to handle button clicks.
    def handle_click(i, j):
        if (i, j) not in board_available(extra=True):
            pass
        elif not st.session_state.winner:
            # TODO: Handle the case when nobody wins but the game is over!
            st.session_state.board[i, j] = st.session_state.player
            # switch the player after the updating the board
            st.session_state.player = (
                "O" if st.session_state.player == "X" else "X"
            )
            winner = check_win(st.session_state.board)
            if winner != ".":
                st.session_state.winner = winner

    # Show one button for each field.
    for i, row in enumerate(st.session_state.board):
        cols = st.columns([5, 1, 1, 1, 5])
        for j, field in enumerate(row):
            cols[j+1].button(
                field,
                key=f"{i}-{j}",
                on_click=handle_click if st.session_state.player == 'X' or st.session_state.opponent == 'Human' else computer_player(),
                args=(i, j),
            )

    check_state()

    score.button(f'❌{st.session_state.win["X"]} 🆚 {st.session_state.win["O"]}⭕')
    player.button(f'{"❌" if st.session_state.player == "X" else "⭕"}\'s turn' if not st.session_state.winner else f'🏁 Game finished')

if __name__ == '__main__':
    play()
