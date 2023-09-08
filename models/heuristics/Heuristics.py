import chess

from Board import Board
import config
from models.heuristics.MoveMap import position_to_score

white_score_dict = {
    'r': -500,
    'n': -320,
    'b': -330, 
    'q': -900,
    'k': 000,
    'p': -100,
    'P': 100,
    'R': 500,
    'N': 320,
    'B': 330, 
    'Q': 900,
    'K': 0
}

def is_endgame(board: Board):
    white_queen_exists = False
    black_queen_exists = False
    piece_count = 0
    for row in board.as_list():
        for c in row:
            if c != '.':
                if c == 'q':
                    black_queen_exists = True
                elif c == 'Q':
                    white_queen_exists = True
                if c not in ['p', 'P', 'k', 'K']:
                    piece_count += white_score_dict[c]
    return not white_queen_exists and not black_queen_exists and (piece_count <= 1160)

def name(ch, is_end):
    if ch not in ['k', 'K']:
        return ch
    if is_end:
        return ch + '_end'
    else:
        return ch + '_middle'

def score(board: Board, color):
    # add wins, losses, draws
    if board.outcome() is not None:
        if board.outcome().winner is None:
            return 0
        elif board.outcome().winner == (color == 'white'):
            return 100000
        else:
            return -100000
    # add piece scores and position scores
    result = 0
    is_end = is_endgame(board)
    for i, row in enumerate(board.as_list()):
        for j, ch in enumerate(row):
            if ch != '.':
                result += white_score_dict[ch]
                result += position_to_score[name(ch, is_end)][i][j]
    # reverse for black
    if color == 'white':
        return result
    else:
        return -result
    
def move_importance(board: Board, move: chess.Move) -> int:
    score = 0
    if board.gives_check(move):
        score += 40
    if board.is_capture(move):
        score += 30
    
    start_row = int(str(move)[1])
    end_row = int(str(move)[3])
    direction_priority = -1 if config.COMPUTER_COLOR == 'black' else 1
    return direction_priority * (end_row - start_row)