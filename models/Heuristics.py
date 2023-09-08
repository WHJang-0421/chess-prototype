import chess

from Board import Board
import config

white_score_dict = {
    'r': -5,
    'n': -3,
    'b': -3, 
    'q': -9,
    'k': 0,
    'p': -1,
    'P': 1,
    'R': 5,
    'N': 3,
    'B': 3, 
    'Q': 9,
    'K': 0
}

def score(board: Board, color):
    if board.outcome() is not None:
        if board.outcome().winner is None:
            return 0
        elif board.outcome().winner == (color == 'white'):
            return 100
        else:
            return -100
    result = 0
    for row in board.as_list():
        for c in row:
            if c != '.':
                result += white_score_dict[c]
    if color == 'white':
        return result
    else:
        return -result