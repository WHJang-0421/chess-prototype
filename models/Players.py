from abc import ABC, abstractmethod
import chess

from Board import Board
import config

class Player(ABC):
    @abstractmethod
    def next_move(self, board: Board) -> chess.Move:
        '''
        Returns next move in pychess format
        '''
        pass

class RandomPlayer(Player):
    def next_move(self, board):
        if list(board.legal_moves):
            return list(board.legal_moves)[0]
        else:
            return None
        
class GreedyPlayer(Player):
    computer_color = config.COMPUTER_COLOR
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

    def next_move(self, board):
        moves = list(board.legal_moves)
        return max(moves, key=lambda x: self.score(board, x))
            

    def score(self, board: Board, move):
        board.push(move)
        result = 0
        for row in board.as_list():
            for c in row:
                if c != '.':
                    result += self.white_score_dict[c]
        board.pop()
        if self.computer_color == 'white':
            return result
        else:
            return -result