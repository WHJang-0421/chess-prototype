import pygame
import chess

import config
import utils as utils
from Board import Board
from Positions import TilePosition, PointPosition

pygame.init()
pygame.display.set_caption('Chess')

# create the chess board
board_screen = pygame.display.set_mode(config.BOARD_SIZE)

# the python chess representation of the board
board = Board()

# a function that draws pieces and circles on the board
def draw_piece(board, screen, circles=None):
    # clear the screen
    screen.fill((0,0,0))
    # draw the tiles
    for row in range(8):
        for col in range(8):
            tile = TilePosition(row, col)
            pygame.draw.rect(board_screen, config.COLOR_RGB[tile.color], pygame.Rect(*tile.top_left_point, *config.TILE_SIZE))
    # draw the pieces
    board_list = board.as_list()
    for row in range(8):
        for col in range(8):
            tile = TilePosition(row, col)
            if board_list[row][col] != '.':
                piece = pygame.image.load(config.piece_files[board_list[row][col]]).convert_alpha()
                screen.blit(piece, PointPosition(*config.IMAGE_PAD) + tile.top_left_point)
    # draw the circles
    if circles is not None:
        for row, col in circles:
            tile = TilePosition(row, col)
            pygame.draw.circle(screen, (100,100,100), list(reversed(tile.center_point)), 5, 0)
    # update the window
    pygame.display.flip()


draw_piece(board, board_screen)

##### game logic
running = True
board_can_change = False
promotion = None
prev_rowcol = ()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and promotion:
            x, y = pygame.mouse.get_pos()
            row, col = utils.tile_row_col(x, y)
            promote_to = 'qrbn'[col]

            move = chess.Move.from_uci(promotion + promote_to)
            board.push(move)
            print(board)
            draw_piece(board, board_screen)
            promotion = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not board_can_change:
            x, y = pygame.mouse.get_pos()
            row, col = utils.tile_row_col(x, y)
            if board.as_list()[row][col] != '.':
                click_pos_str = utils.position_str(row, col)
                circles = []
                for move in board.legal_moves:
                    if str(move)[:2] == click_pos_str:
                        circles.append(utils.position_str_to_rowcol(str(move)[2:]))

                draw_piece(board, board_screen, circles)
                prev_rowcol = (row, col)
                board_can_change = True
        elif event.type == pygame.MOUSEBUTTONDOWN and board_can_change:
            x, y = pygame.mouse.get_pos()
            row, col = utils.tile_row_col(x, y)
            if (row == prev_rowcol[0] and col == prev_rowcol[1]):
                break
            move = chess.Move.from_uci(utils.position_str(*prev_rowcol) + utils.position_str(row, col))
            if move in board.legal_moves:
                board.push(move)
                print(board)
                draw_piece(board, board_screen)
            elif chess.Move.from_uci(str(move) + 'r') in board.legal_moves:
                # display screen to choose between promotion pieces
                pygame.draw.rect(board_screen, (255,255,255), pygame.Rect(0, 0, 4*config.TILE_SIZE[1], config.TILE_SIZE[0]))
                # queen, rook, bishop, knight
                for i, c in enumerate('qrbn'):
                    piece = pygame.image.load(config.piece_files[c]).convert_alpha()
                    board_screen.blit(piece, (config.IMAGE_PAD[0] + utils.position(0, i)[0], config.IMAGE_PAD[1] + utils.position(0, i)[1]))
                pygame.display.flip()
                prev_rowcol = (row, col)
                promotion = str(move)
            board_can_change = False
        elif event.type == pygame.MOUSEBUTTONUP:
            print('end click')

        # check if the game ended
        if board.outcome() is not None:
            if board.outcome().result() == '1-0':
                result = 'white wins'
            elif board.outcome().result() == '0-1':
                result = 'black wins'
            else:
                result = 'draw'
                
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(result, True, (0,0,0), (255,255,255))
            text_rect = text.get_rect()
            text_rect.center = (360, 360)
            board_screen.blit(text, text_rect)
            pygame.display.flip()