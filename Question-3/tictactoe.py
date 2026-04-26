import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        values = [board[i][j] for i, j in line]
        if values[0] == values[1] == values[2] != EMPTY:
            return values[0]
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    return all(cell != EMPTY for row in board for cell in row)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = float("-inf")
        for action in actions(state):
            v = max(v, min_value(result(state, action)))
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = float("inf")
        for action in actions(state):
            v = min(v, max_value(result(state, action)))
        return v

    current = player(board)
    best_action = None

    if current == X:
        best_score = float("-inf")
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
    else:
        best_score = float("inf")
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action

    return best_action