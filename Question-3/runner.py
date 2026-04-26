from tictactoe import initial_state, player, actions, result, terminal, utility, minimax, X, O, EMPTY

def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(cell if cell else " " for cell in row))
        if i < 2:
            print("---+---+---")
    print()

def get_human_move(board):
    while True:
        try:
            move = input("Enter move as row col (0-2): ").strip()
            i, j = map(int, move.split())
            if (i, j) in actions(board):
                return (i, j)
            print("Invalid move.")
        except Exception:
            print("Enter two numbers 0-2 separated by a space.")

def play_game():
    board = initial_state()
    print("Human is X, AI is O.")
    while not terminal(board):
        print_board(board)
        if player(board) == X:
            board = result(board, get_human_move(board))
        else:
            action = minimax(board)
            board = result(board, action)
            print(f"AI plays: {action}")
    print_board(board)
    if utility(board) == 1:
        print("X wins!")
    elif utility(board) == -1:
        print("O wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    play_game()