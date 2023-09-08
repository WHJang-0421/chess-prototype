import chess
import chess.polyglot

from models.Players import Player, white_score_dict
from Board import Board
from models.heuristics.Heuristics import score
import config

class Node:
    def __init__(self, board: Board, prev_move, is_max: bool):
        self.board = board
        self.prev_move = prev_move
        self.evaluation = None
        self.is_max = is_max
        self.next_node = None
        self.childs = []

class MinMax(Player):
    computer_color = config.COMPUTER_COLOR

    def __init__(self, depth=5):
        self.total_depth = depth

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
        for c in node.childs:
            self.evaluate(c, depth-1)
        if node.is_max:
            node.next_node = max(node.childs, key=lambda x: x.evaluation)
        else:
            node.next_node = min(node.childs, key=lambda x: x.evaluation)
        node.evaluation = node.next_node.evaluation

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