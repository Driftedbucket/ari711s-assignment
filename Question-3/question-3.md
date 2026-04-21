Ǫuestion 3: Adversarial Search [25 Marks]
Using Minimax, implement an AI to play Tic-Tac-Toe optimally.
Figure 1: Tic-Tac Toe Graphica Interface.
Background
In practical lab 2, we explored the fundamentals of decision-making in adversarial environments through basic search problems. In this task, you will apply what you have learnt to build an AI agent that plays Tic Tac Toe optimally using the Minimax algorithm. You will implement the complete game logic for Tic-Tac Toe from scratch, including all the helper functions necessary for evaluating game states, determining optimal actions, and simulating turns. Your AI should be unbeatable when playing against any opponent, provided it always plays optimally.
Understanding the problem
This problem can be framed as a two-player deterministic adversarial game, where:
•
States are 3×3 game boards.
•
Actions are available positions (i, j) where a player can move.
• The player alternates between X and O'.
•
Terminal states occur when the board is full or when a player has won.
• Utility is +1 for a win by X, for a win by O, and 0 for a tie.
•
Your agent will use the Minimax algorithm to determine the best move from any given board configuration.
Specification
Your program must implement the following core components:
False
result
board
O
player
•
The function that takes a board state as input and returns which player’s turn it is
(either X or O).
o
In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
o
Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
•
The
given board.
function returns a set of all of the possible actions that can be taken on a
o
Each action should be represented as a tuple (i, j) where i corresponds to the row
of the move ( the move (0,
, or 2) and j corresponds to which cell in the row corresponds to
, or 2).
o
Possible moves are any cells on the board that do not already have an X or an in them.
o
Any return value is acceptable if a terminal board is provided as input.
•
The
function takes a
and an
as input and should return a new board
state without modifying the original board.
o
If the exception.
is not a valid action for the board, your program should raise an
o
The returned board state should be the board that would result from taking the original input board and letting the player whose turn it is make their move at the cell indicated by the input action.
o
Importantly, the original board should be left unmodified since Minimax will ultimately require considering many different board states during its
computation. This means that simply updating a cell in the itself is not a
correct implementation of the function. You will likely want to make a deep
copy of the board first before making any changes.
•
The
function should accept a
as input and return the winner of the board if
there is one.
o
If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
o
One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
o
You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
o
If there is no winner of the game (either because the game is in progress or because it ended in a tie), the function should return None.
•
The
function should accept a
as input and return a boolean value
indicating whether the game is over.
o
If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
o
Otherwise, the function should return if the game is still in progress.
•
The board.
function should accept a terminal board as input and output the utility of the
o
If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
o
You may assume utility will only be called on a board if the terminal(board) is True.
•
The
function should take a
as input and return the optimal move for the
player to move on that board.
board
minimax
utility
board
terminal
board
winner
action
action
board
result
actions 0 , 1 1
runner.py
tictactoe.py
runner.py
board
(i, j),
o
The move returned should be the optimal action which is one of the
allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
o
If the
is a terminal board, the
function should return None.
For all functions that accept a as input, you may assume that it is a valid board (namely,
that it is a list that contains three rows, each with three values of either X, O, or EMPTY).
Testing
You test your AI in a graphical interface, by writing a that:
•
Displays the board in the terminal or using a GUI (e.g., tkinter).
•
Allows a human player to play against the AI.
•
Displays a message when the game ends.
Hint
•
If you’d like to test your functions in a different Python file, you can import them with lines like from tictactoe import initial_state.
•
Feel free to have as many helper functions as you see fit.
•
Alpha-beta pruning is optional but may make your AI run more efficiently!
Deliverables
You should submit:
•
with all required functions implemented
•
Sample output showing your AI playing from different board states
•
file for testing or demonstration
minimax
board