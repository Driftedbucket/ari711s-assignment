# Question 3 Explanation

## Problem

The task is to build an optimal Tic-Tac-Toe AI using the Minimax algorithm. Tic-Tac-Toe is a two-player deterministic game played on a 3×3 board. Players alternate placing X and O, and the game ends when one player gets three in a row horizontally, vertically, or diagonally, or when the board is full and the game is a tie.

The AI must:
- determine whose turn it is,
- list valid moves,
- simulate moves without changing the original board,
- detect a winner,
- detect terminal game states,
- evaluate terminal boards using utility values,
- choose the optimal move from any board state.

## Solution

The implementation in `tictactoe.py` provides the required functions:

- `player(board)`: counts X and O marks and returns the next player.
- `actions(board)`: returns a set of empty board positions as valid moves.
- `result(board, action)`: returns a new board after applying the move, using a deep copy.
- `winner(board)`: checks all rows, columns, and diagonals for three in a row.
- `terminal(board)`: returns `True` when the game is over.
- `utility(board)`: returns `1` for X win, `-1` for O win, `0` for a tie.
- `minimax(board)`: searches all possible future moves and selects the optimal action.

### How Minimax works

Minimax evaluates the game tree recursively:
- If the current board is terminal, return its utility.
- If X is moving, choose the action that maximizes the score.
- If O is moving, choose the action that minimizes the score.
