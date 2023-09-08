import chess
import chess.polyglot

from models.Players import Player, white_score_dict
from Board import Board
from models.Heuristics import score
import config

class Node:
    def __init__(self, board, prev_move):
        self.board = board
        self.prev_move = prev_move
        self.childs = []

class MinMax(Player):
    computer_color = config.COMPUTER_COLOR

    def __init__(self, depth=5):
        self.total_depth = depth

    def next_move(self, board):
        root = self.create_tree(board, self.total_depth, None)
        return max(root.childs, key=lambda x: self.calculate_score(x, 'min')).prev_move

    def create_tree(self, board: Board, depth, prev_move) -> Node:
        if depth == 0:
            return None
        
        root = Node(board.copy(), prev_move)
        for move in board.legal_moves:
            board.push(move)
            child = self.create_tree(board, depth-1, move)
            if child is not None:
                root.childs.append(child)
            board.pop()
        return root

    def calculate_score(self, node: Node, mode) -> int:
        if not node.childs:
            return score(node.board, self.computer_color)
        if mode == 'max':
            return max([self.calculate_score(child, 'min') for child in node.childs])
        else:
            return min([self.calculate_score(child, 'max') for child in node.childs])
        
class MinMaxWithOpening(Player):
    def __init__(self, depth):
        self.minmax = MinMax(depth)

    def next_move(self, board: Board):
        with chess.polyglot.open_reader("data/Titans.bin") as reader:
            entry = reader.get(board)
            if entry is None:
                return self.minmax.next_move(board)
            else:
                return entry.move