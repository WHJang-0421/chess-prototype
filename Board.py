import chess

class Board(chess.Board):
    def as_list(self):
        board_list = [['' for _ in range(8)] for _ in range(8)]
        i = 0
        for c in str(self):
            if not c.isspace():
                board_list[i//8][i%8] = c
                i += 1
        return board_list