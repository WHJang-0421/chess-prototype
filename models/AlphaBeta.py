import chess
import chess.polyglot

from models.Players import Player, white_score_dict
from Board import Board
from models.Heuristics import score
from models.MinMax import MinMaxNode
import config

class AlphaBetaPruner(Player):
    computer_color = config.COMPUTER_COLOR

    def __init__(self, depth=5):
        self.total_depth = depth
        self.alpha = None
        self.beta = None

    def next_move(self, board: Board):
        root = self.create_tree(board, self.total_depth, None, 'max')
        self.evaluate(root)
        return root.next_node.prev_move
    
    def evaluate(self, node: MinMaxNode, depth):
        if node.evaluation is not None:
            return
        
        if depth == 0:
            node.evaluation = score(node.board, config.COMPUTER_COLOR)
            return

        # create childs
        node.childs = [MinMaxNode(node.board.copy().push(move), move, 'min' if node.type == 'max' else 'max') for move in node.board.legal_moves]
        
