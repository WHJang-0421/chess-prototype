import pygame
import chess

import config
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
promotion_move = None
moving_piece_start_position = ()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = PointPosition(*pygame.mouse.get_pos())
            selected_tile = TilePosition.from_position(*mouse_position)

            if promotion_move and selected_tile.col < 4:
                print('1')
                promote_to = 'qrbn'[selected_tile.col]
                move = chess.Move.from_uci(promotion_move + promote_to)
                board.push(move)
                draw_piece(board, board_screen)
                # update loop variables
                board_can_change = False
                promotion_move = None
                moving_piece_start_position = ()

            elif not board_can_change and board.as_list()[selected_tile.row][selected_tile.col] != '.':
                print('2')
                circles = []
                for move in board.legal_moves:
                    if str(move)[:2] == str(selected_tile):
                        circles.append(TilePosition.from_string(str(move)[2:]))
                draw_piece(board, board_screen, circles)
                # update loop variables
                moving_piece_start_position = selected_tile
                board_can_change = True if circles else False
                promotion_move = None

            elif board_can_change and selected_tile != moving_piece_start_position:
                print('3')
                move = chess.Move.from_uci(str(moving_piece_start_position) + str(selected_tile))
                if move in board.legal_moves:
                    board.push(move)
                    draw_piece(board, board_screen)
                    board_can_change = False
                    moving_piece_start_position = ()
                    promotion_move = ()
                elif chess.Move.from_uci(str(move) + 'r') in board.legal_moves:
                    # display screen to choose between promotion pieces
                    pygame.draw.rect(board_screen, (255,255,255), pygame.Rect(0, 0, 4*config.TILE_SIZE[1], config.TILE_SIZE[0]))
                    for i, c in enumerate('qrbn'):
                        piece = pygame.image.load(config.piece_files[c]).convert_alpha()
                        board_screen.blit(piece, TilePosition(0,i).top_left_point + PointPosition(*config.IMAGE_PAD))
                    pygame.display.flip()
                    board_can_change = False
                    moving_piece_start_position = ()
                    promotion_move = str(move)
                else:
                    board_can_change = True
                

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