from abc import ABC, abstractmethod
import chess

from Board import Board
from models.Heuristics import white_score_dict, score
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

    def next_move(self, board):
        moves = list(board.legal_moves)
        return max(moves, key=lambda x: self.score(board, x))
            

    def score(self, board: Board, move):
        board.push(move)
        result = score(board, self.computer_color)
        board.pop()
        return result