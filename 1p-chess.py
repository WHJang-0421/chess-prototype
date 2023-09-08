import pygame
import chess

import config
from Board import Board
from Positions import TilePosition, PointPosition
from models.AlphaBeta import AlphaBetaWithOpening

pygame.init()
pygame.display.set_caption('Chess')

# create the chess board
screen = pygame.display.set_mode(config.BOARD_SIZE)

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
            pygame.draw.rect(screen, config.COLOR_RGB[tile.color], pygame.Rect(*tile.top_left_point, *config.TILE_SIZE))
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


draw_piece(board, screen)

##### game logic
computer_agent = AlphaBetaWithOpening(3)
current_player = 'white'
running = True
board_can_change = False
promotion_move = None
moving_piece_start_position = ()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif current_player == config.COMPUTER_COLOR and board.outcome() is None:
            move = computer_agent.next_move(board)
            board.push(move)
            draw_piece(board, screen)
            current_player = config.PLAYER_COLOR

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = PointPosition(*pygame.mouse.get_pos())
            selected_tile = TilePosition.from_position(*mouse_position)

            if promotion_move and config.BOARD_SIZE[1]/2 - 2*config.TILE_SIZE[1] <= mouse_position.x <=  config.BOARD_SIZE[1]/2 + 2*config.TILE_SIZE[1] and config.BOARD_SIZE[0]/2 - 0.5*config.TILE_SIZE[0] <= mouse_position.y <= config.BOARD_SIZE[0]/2 + 0.5*config.TILE_SIZE[0]:
                promote_to = 'qrbn'[int((mouse_position.x - (config.BOARD_SIZE[1]/2 - 2*config.TILE_SIZE[1])) // (config.TILE_SIZE[1]))]
                move = chess.Move.from_uci(promotion_move + promote_to)
                board.push(move)
                draw_piece(board, screen)
                # update loop variables
                board_can_change = False
                promotion_move = None
                moving_piece_start_position = ()
                current_player = config.COMPUTER_COLOR

            elif board_can_change and selected_tile != moving_piece_start_position:
                move = chess.Move.from_uci(str(moving_piece_start_position) + str(selected_tile))
                if move in board.legal_moves:
                    board.push(move)
                    draw_piece(board, screen)
                    board_can_change = False
                    moving_piece_start_position = ()
                    promotion_move = ()
                    current_player = config.COMPUTER_COLOR
                elif chess.Move.from_uci(str(move) + 'r') in board.legal_moves:
                    # display screen to choose between promotion pieces
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(config.BOARD_SIZE[1]/2 - 2*config.TILE_SIZE[1], config.BOARD_SIZE[0]/2 - 0.5*config.TILE_SIZE[0], 4*config.TILE_SIZE[1], config.TILE_SIZE[0]))
                    for i, c in enumerate('qrbn'):
                        piece = pygame.image.load(config.piece_files[c]).convert_alpha()
                        screen.blit(piece, PointPosition(config.BOARD_SIZE[1]/2 + (i-2)*config.TILE_SIZE[1], config.BOARD_SIZE[0]/2 - 0.5*config.TILE_SIZE[0]) + PointPosition(*config.IMAGE_PAD))
                    pygame.display.flip()
                    board_can_change = True
                    moving_piece_start_position = ()
                    promotion_move = str(move)
                    current_player = config.PLAYER_COLOR
                else:
                    current_player = config.PLAYER_COLOR
                    board_can_change = False
                    draw_piece(board, screen)

            if not board_can_change and board.as_list()[selected_tile.row][selected_tile.col] != '.' and current_player == config.PLAYER_COLOR:
                circles = []
                for move in board.legal_moves:
                    if str(move)[:2] == str(selected_tile):
                        circles.append(TilePosition.from_string(str(move)[2:]))
                draw_piece(board, screen, circles)
                # update loop variables
                moving_piece_start_position = selected_tile
                board_can_change = True if circles else False
                promotion_move = None
                current_player = config.PLAYER_COLOR
                

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
            screen.blit(text, text_rect)
            pygame.display.flip()