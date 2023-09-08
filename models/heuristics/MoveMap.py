# the value of piece positions on the board
# the score is for white

position_to_score = {
    'P':  [[0, 0, 0, 0, 0, 0, 0, 0], 
        [50, 50, 50, 50, 50, 50, 50, 50], 
        [10, 10, 20, 30, 30, 20, 10, 10], 
        [5, 5, 10, 25, 25, 10, 5, 5], 
        [0, 0, 0, 20, 20, 0, 0, 0], 
        [5, -5, -10, 0, 0, -10, -5, 5], 
        [5, 10, 10, -20, -20, 10, 10, 5], 
        [0, 0, 0, 0, 0, 0, 0, 0]],
    'p': list(reversed([[0, 0, 0, 0, 0, 0, 0, 0], 
        [-50, -50, -50, -50, -50, -50, -50, -50], 
        [-10, -10, -20, -30, -30, -20, -10, -10], 
        [-5, -5, -10, -25, -25, -10, -5, -5], 
        [0, 0, 0, -20, -20, 0, 0, 0], 
        [-5, 5, 10, 0, 0, 10, 5, -5], 
        [-5, -10, -10, 20, 20, -10, -10, -5], 
        [0, 0, 0, 0, 0, 0, 0, 0]])),
    'N':  [[-50,-40,-30,-30,-30,-30,-40,-50,],
           [-40,-20,  0,  0,  0,  0,-20,-40,],
           [-30,  0, 10, 15, 15, 10,  0,-30,],
           [-30,  5, 15, 20, 20, 15,  5,-30,],
           [-30,  0, 15, 20, 20, 15,  0,-30,],
           [-30,  5, 10, 15, 15, 10,  5,-30,],
           [-40,-20,  0,  5,  5,  0,-20,-40,],
           [-50,-40,-30,-30,-30,-30,-40,-50,]],
    'n': list(reversed([[50, 40, 30, 30, 30, 30, 40, 50], 
        [40, 20, 0, 0, 0, 0, 20, 40], 
        [30, 0, -10, -15, -15, -10, 0, 30], 
        [30, -5, -15, -20, -20, -15, -5, 30], 
        [30, 0, -15, -20, -20, -15, 0, 30], 
        [30, -5, -10, -15, -15, -10, -5, 30], 
        [40, 20, 0, -5, -5, 0, 20, 40], 
        [50, 40, 30, 30, 30, 30, 40, 50]])),
    'B':[[-20,-10,-10,-10,-10,-10,-10,-20,],
        [-10,  0,  0,  0,  0,  0,  0,-10,],
        [-10,  0,  5, 10, 10,  5,  0,-10,],
        [-10,  5,  5, 10, 10,  5,  5,-10,],
        [-10,  0, 10, 10, 10, 10,  0,-10,],
        [-10, 10, 10, 10, 10, 10, 10,-10,],
        [-10,  5,  0,  0,  0,  0,  5,-10,],
        [-20,-10,-10,-10,-10,-10,-10,-20,],],
    'b': list(reversed([[20, 10, 10, 10, 10, 10, 10, 20], 
        [10, 0, 0, 0, 0, 0, 0, 10], 
        [10, 0, -5, -10, -10, -5, 0, 10], 
        [10, -5, -5, -10, -10, -5, -5, 10], 
        [10, 0, -10, -10, -10, -10, 0, 10], 
        [10, -10, -10, -10, -10, -10, -10, 10], 
        [10, -5, 0, 0, 0, 0, -5, 10], 
        [20, 10, 10, 10, 10, 10, 10, 20]])),
    'R': [[0, 0, 0, 0, 0, 0, 0, 0], 
        [5, 10, 10, 10, 10, 10, 10, 5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [0, 0, 0, 5, 5, 0, 0, 0]],
    'r': list(reversed([[0, 0, 0, 0, 0, 0, 0, 0], 
        [-5, -10, -10, -10, -10, -10, -10, -5], 
        [5, 0, 0, 0, 0, 0, 0, 5], 
        [5, 0, 0, 0, 0, 0, 0, 5], 
        [5, 0, 0, 0, 0, 0, 0, 5], 
        [5, 0, 0, 0, 0, 0, 0, 5], 
        [5, 0, 0, 0, 0, 0, 0, 5], 
        [0, 0, 0, -5, -5, 0, 0, 0]])),
    'Q': [[-20, -10, -10, -5, -5, -10, -10, -20], 
        [-10, 0, 0, 0, 0, 0, 0, -10], 
        [-10, 0, 5, 5, 5, 5, 0, -10], 
        [-5, 0, 5, 5, 5, 5, 0, -5], 
        [0, 0, 5, 5, 5, 5, 0, -5], 
        [-10, 5, 5, 5, 5, 5, 0, -10], 
        [-10, 0, 5, 0, 0, 0, 0, -10], 
        [-20, -10, -10, -5, -5, -10, -10, -20]],
    'q': list(reversed([[20, 10, 10, 5, 5, 10, 10, 20], 
        [10, 0, 0, 0, 0, 0, 0, 10], 
        [10, 0, -5, -5, -5, -5, 0, 10], 
        [5, 0, -5, -5, -5, -5, 0, 5], 
        [0, 0, -5, -5, -5, -5, 0, 5], 
        [10, -5, -5, -5, -5, -5, 0, 10], 
        [10, 0, -5, 0, 0, 0, 0, 10], 
        [20, 10, 10, 5, 5, 10, 10, 20]])),
    'K_middle': [[-30, -40, -40, -50, -50, -40, -40, -30], 
                [-30, -40, -40, -50, -50, -40, -40, -30], 
                [-30, -40, -40, -50, -50, -40, -40, -30], 
                [-30, -40, -40, -50, -50, -40, -40, -30], 
                [-20, -30, -30, -40, -40, -30, -30, -20], 
                [-10, -20, -20, -20, -20, -20, -20, -10], 
                [20, 20, 0, 0, 0, 0, 20, 20], 
                [20, 30, 10, 0, 0, 10, 30, 20]],
    'k_middle': list(reversed([[30, 40, 40, 50, 50, 40, 40, 30], 
                [30, 40, 40, 50, 50, 40, 40, 30], 
                [30, 40, 40, 50, 50, 40, 40, 30], 
                [30, 40, 40, 50, 50, 40, 40, 30], 
                [20, 30, 30, 40, 40, 30, 30, 20], 
                [10, 20, 20, 20, 20, 20, 20, 10], 
                [-20, -20, 0, 0, 0, 0, -20, -20], 
                [-20, -30, -10, 0, 0, -10, -30, -20]])),
    'K_end': [[-50, -40, -30, -20, -20, -30, -40, -50], 
            [-30, -20, -10, 0, 0, -10, -20, -30], 
            [-30, -10, 20, 30, 30, 20, -10, -30], 
            [-30, -10, 30, 40, 40, 30, -10, -30], 
            [-30, -10, 30, 40, 40, 30, -10, -30], 
            [-30, -10, 20, 30, 30, 20, -10, -30], 
            [-30, -30, 0, 0, 0, 0, -30, -30], 
            [-50, -30, -30, -30, -30, -30, -30, -50]],
    'k_end': list(reversed([[50, 40, 30, 20, 20, 30, 40, 50], 
            [30, 20, 10, 0, 0, 10, 20, 30], 
            [30, 10, -20, -30, -30, -20, 10, 30], 
            [30, 10, -30, -40, -40, -30, 10, 30], 
            [30, 10, -30, -40, -40, -30, 10, 30], 
            [30, 10, -20, -30, -30, -20, 10, 30], 
            [30, 30, 0, 0, 0, 0, 30, 30], 
            [50, 30, 30, 30, 30, 30, 30, 50]]))
}