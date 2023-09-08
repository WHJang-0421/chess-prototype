import chess
import chess.polyglot

from models.Players import Player, white_score_dict
from Board import Board
from models.Heuristics import score
from models.MinMax import Node
import config

class AlphaBeta(Player):
    computer_color = config.COMPUTER_COLOR

    def __init__(self, depth=5):
        self.total_depth = depth
        self.alpha = -10000
        self.beta = 10000

    def next_move(self, board):
        root = Node(board, None, True)
        self.evaluate(root, self.total_depth)
        return root.next_node.prev_move

    def evaluate(self, node: Node, depth) -> None:
        if node.evaluation:
            return
        
        if depth == 0:
            node.evaluation = score(node.board, self.computer_color)
            return

        for move in node.board.legal_moves:
            new_board = node.board.copy()
            new_board.push(move)
            node.childs.append(Node(new_board, move, not node.is_max))

        if not node.is_max:
            pruned = False
            for c in node.childs:
                self.evaluate(c, depth-1)
                if c.evaluation < self.alpha:
                    node.evaluation = -10000
                    pruned = True
                    break
            if not pruned:
                node.next_node = min(node.childs, key=lambda x: x.evaluation)
                node.evaluation = node.next_node.evaluation
                self.beta = max(node.evaluation, self.beta)
        else:
            pruned = False
            for c in node.childs:
                self.evaluate(c, depth-1)
                if c.evaluation > self.beta:
                    node.evaluation = 10000
                    pruned = True
                    break
            if not pruned:
                node.next_node = max(node.childs, key=lambda x: x.evaluation)
                node.evaluation = node.next_node.evaluation
                self.alpha = min(node.evaluation, self.alpha)

        return