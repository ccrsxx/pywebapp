import streamlit as st
import numpy as np
import random


def init(post_init=False):
    if not post_init:
        st.session_state.opponent = 'Human'
        st.session_state.win = {'X': 0, 'O': 0}
    st.session_state.board = np.full((3, 3), '.', dtype=str)
    st.session_state.player = 'X'
    st.session_state.warning = False
    st.session_state.winner = None
    st.session_state.over = False


def check_available_moves(extra=False) -> list:
    raw_moves = [row for col in st.session_state.board.tolist() for row in col]
    num_moves = [i for i, spot in enumerate(raw_moves) if spot == '.']
    if extra:
        return [(i // 3, i % 3) for i in num_moves]
    return num_moves


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


def check_state():
    if st.session_state.winner:
        st.success(f"Congrats! {st.session_state.winner} won the game! 🎈")
    if st.session_state.warning and not st.session_state.over:
        st.warning('⚠️ This move already exist')
    if st.session_state.winner and not st.session_state.over:
        st.session_state.over = True
        st.session_state.win[st.session_state.winner] = (
            st.session_state.win.get(st.session_state.winner, 0) + 1
        )
    elif not check_available_moves() and not st.session_state.winner:
        st.info(f'It\'s a tie 📍')
        st.session_state.over = True


def check_win(board):
    for new_board in [board, np.transpose(board)]:
        result = check_rows(new_board)
        if result:
            return result
    return check_diagonals(board)


def computer_player():
    moves = check_available_moves(extra=True)
    if moves:
        i, j = random.choice(moves)
        handle_click(i, j)


def handle_click(i, j):
    if (i, j) not in check_available_moves(extra=True):
        st.session_state.warning = True
    elif not st.session_state.winner:
        st.session_state.warning = False
        st.session_state.board[i, j] = st.session_state.player
        st.session_state.player = "O" if st.session_state.player == "X" else "X"
        winner = check_win(st.session_state.board)
        if winner != ".":
            st.session_state.winner = winner


def main():
    st.write(
        """
        # ❎🅾️ Tic Tac Toe
        """
    )

    if "board" not in st.session_state:
        init()

    reset, score, player, settings = st.columns([0.5, 0.6, 1, 1])
    reset.button('New game', on_click=init, args=(True,))

    with settings.expander('Settings'):
        st.write('**Warning**: changing this setting will restart your game')
        st.selectbox(
            'Set opponent',
            ['Human', 'Computer'],
            key='opponent',
            on_change=init,
            args=(True,),
        )

    for i, row in enumerate(st.session_state.board):
        cols = st.columns([5, 1, 1, 1, 5])
        for j, field in enumerate(row):
            cols[j + 1].button(
                field,
                key=f"{i}-{j}",
                on_click=handle_click
                if st.session_state.player == 'X'
                or st.session_state.opponent == 'Human'
                else computer_player(),
                args=(i, j),
            )

    check_state()

    score.button(f'❌{st.session_state.win["X"]} 🆚 {st.session_state.win["O"]}⭕')
    player.button(
        f'{"❌" if st.session_state.player == "X" else "⭕"}\'s turn'
        if not st.session_state.winner
        else f'🏁 Game finished'
    )


if __name__ == '__main__':
    main()
