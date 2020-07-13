import pygame
import random
from Chess import ChessGame, Piece, King, Queen, Rook, Bishop, Knight, Pawn, format_to_nums, format_to_let
from Engine import Engine

pygame.init()

display_width = 512
display_height = 512

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Chess')
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
board = pygame.image.load("images/board.png")
game = ChessGame()

white_pawn_img = pygame.image.load('images/white-pawn.png')
white_bishop_img = pygame.image.load("images/white-bishop.png")
white_knight_img = pygame.image.load("images/white-knight.png")
white_rook_img = pygame.image.load("images/white-rook.png")
white_queen_img = pygame.image.load("images/white-queen.png")
white_king_img = pygame.image.load("images/white-king.png")

black_pawn_img = pygame.image.load('images/black-pawn.png')
black_bishop_img = pygame.image.load("images/black-bishop.png")
black_knight_img = pygame.image.load("images/black-knight.png")
black_rook_img = pygame.image.load("images/black-rook.png")
black_queen_img = pygame.image.load("images/black-queen.png")
black_king_img = pygame.image.load("images/black-king.png")
game = ChessGame()
engine = Engine(game)


def format_to_8x8(alg_coord):
    """formats an algebraic chess coordinate to 8x8 coord in 512x512 window"""
    let = alg_coord[0]
    num = int(alg_coord[1])
    file = (ord(let) - 97) * (512 // 8)
    rank = (abs(8-num)) * (512 // 8)
    return rank, file


def promotion(piece_to_move):
    done = False
    while not done:
        pygame.display.flip()  # update display
        window.blit(board, (0, 0))  # draw board (this erases former positions of pieces
        draw_pieces()  # draw each piece in the piece list to the appropriate position
        mx, my = pygame.mouse.get_pos()

        if piece_to_move.get_color() == "white":
            knight_rect = pygame.draw.rect(window, (0, 0, 0), (16, 64 + 16, 96, 96))
            window.blit(white_knight_img, (display_width / 4 * 0 + 32, 32 + 64))

            bishop_rect = pygame.draw.rect(window, black, (display_width / 4 * 1 + 16, 64 + 16, 96, 96))
            window.blit(white_bishop_img, (display_width / 4 * 1 + 32, 32 + 64))

            rook_rect = pygame.draw.rect(window, black, (display_width / 4 * 2 + 16, 64 + 16, 96, 96))
            window.blit(white_rook_img, (display_width / 4 * 2 + 32, 32 + 64))

            queen_rect = pygame.draw.rect(window, black, (display_width / 4 * 3 + 16, 64 + 16, 96, 96))
            window.blit(white_queen_img, (display_width / 4 * 3 + 32, 32 + 64))

            if knight_rect.collidepoint(mx, my):
                knight_rect = pygame.draw.rect(window, (40, 40, 40), (16, 64 + 16, 96, 96))
                window.blit(white_knight_img, (display_width / 4 * 0 + 32, 32 + 64))

            if bishop_rect.collidepoint(mx, my):
                bishop_rect = pygame.draw.rect(window, (40, 40, 40),  (display_width / 4 * 1 + 16, 64 + 16, 96, 96))
                window.blit(white_bishop_img, (display_width / 4 * 1 + 32, 32 + 64))

            if rook_rect.collidepoint(mx, my):
                rook_rect = pygame.draw.rect(window, (40, 40, 40), (display_width / 4 * 2 + 16, 64 + 16, 96, 96))
                window.blit(white_rook_img, (display_width / 4 * 2 + 32, 32 + 64))

            if queen_rect.collidepoint(mx, my):
                queen_rect = pygame.draw.rect(window, (40, 40, 40), (display_width / 4 * 3 + 16, 64 + 16, 96, 96))
                window.blit(white_queen_img, (display_width / 4 * 3 + 32, 32 + 64))

        if piece_to_move.get_color() == "black":
            knight_rect = pygame.draw.rect(window, white, (16, 64 + 16, 96, 96))
            window.blit(black_knight_img, (display_width / 4 * 0 + 32, 32 + 64))

            bishop_rect = pygame.draw.rect(window, white, (display_width / 4 * 1 + 16, 64 + 16, 96, 96))
            window.blit(black_bishop_img, (display_width / 4 * 1 + 32, 32 + 64))

            rook_rect = pygame.draw.rect(window, white, (display_width / 4 * 2 + 16, 64 + 16, 96, 96))
            window.blit(black_rook_img, (display_width / 4 * 2 + 32, 32 + 64))

            queen_rect = pygame.draw.rect(window, white, (display_width / 4 * 3 + 16, 64 + 16, 96, 96))
            window.blit(black_queen_img, (display_width / 4 * 3 + 32, 32 + 64))

            if knight_rect.collidepoint(mx, my):
                knight_rect = pygame.draw.rect(window, (200, 200, 200), (16, 64 + 16, 96, 96))
                window.blit(black_knight_img, (display_width / 4 * 0 + 32, 32 + 64))

            if bishop_rect.collidepoint(mx, my):
                bishop_rect = pygame.draw.rect(window, (200, 200, 200), (display_width / 4 * 1 + 16, 64 + 16, 96, 96))
                window.blit(black_bishop_img, (display_width / 4 * 1 + 32, 32 + 64))

            if rook_rect.collidepoint(mx, my):
                rook_rect = pygame.draw.rect(window, (200, 200, 200), (display_width / 4 * 2 + 16, 64 + 16, 96, 96))
                window.blit(black_rook_img, (display_width / 4 * 2 + 32, 32 + 64))

            if queen_rect.collidepoint(mx, my):
                queen_rect = pygame.draw.rect(window, (200, 200, 200), (display_width / 4 * 3 + 16, 64 + 16, 96, 96))
                window.blit(black_queen_img, (display_width / 4 * 3 + 32, 32 + 64))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if knight_rect.collidepoint(mx, my):
                    piece_to_move.set_promote_to("N")

                if bishop_rect.collidepoint(mx, my):
                    piece_to_move.set_promote_to("B")

                if rook_rect.collidepoint(mx, my):
                    piece_to_move.set_promote_to("R")

                if queen_rect.collidepoint(mx, my):
                    piece_to_move.set_promote_to("Q")
                done = True


def mouse_drag(piece_to_move):
    """
    upon mouse click, erase the piece to move's picture
    place a picture of the piece to move on mouse location
    return control to game_loop
    :param piece_to_move: piece image to blit to mouse position
    :return: none
    """
    while True:
        print(piece_to_move)
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            window.blit(white_pawn_img, (mx, my))
            if event.type == pygame.MOUSEBUTTONUP:
                break


def draw_pieces():
    """draw each piece in game.piece_list """
    for piece in game.get_piece_list():
        if piece.get_color() == "white":
            if piece.get_callsign() == "P":
                window.blit(white_pawn_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "B":
                window.blit(white_bishop_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "N":
                window.blit(white_knight_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "R":
                window.blit(white_rook_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "Q":
                window.blit(white_queen_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "K":
                window.blit(white_king_img, (piece.get_file() * 64, piece.get_rank() * 64))

        if piece.get_color() == "black":
            if piece.get_callsign() == "P":
                window.blit(black_pawn_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "B":
                window.blit(black_bishop_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "N":
                window.blit(black_knight_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "R":
                window.blit(black_rook_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "Q":
                window.blit(black_queen_img, (piece.get_file() * 64, piece.get_rank() * 64))
            if piece.get_callsign() == "K":
                window.blit(black_king_img, (piece.get_file() * 64, piece.get_rank() * 64))


def game_loop():

    done = False
    while not done:
        pygame.display.flip()  # update display
        window.blit(board, (0, 0))  # draw board (this erases former positions of pieces
        draw_pieces()  # draw each piece in the piece list to the appropriate position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # if mouse_down_bool:
                # mx, my = pygame.mouse.get_pos()
                # window.blit(white_pawn_img, (mx, my))

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_down = event
                # assign piece_to_move
                square_from = format_to_let(mouse_down.pos[1] // 64, mouse_down.pos[0] // 64)
                coord_from = format_to_nums(square_from)
                x = game.get_board()[coord_from[0]][coord_from[1]]
                if game.get_board()[coord_from[0]][coord_from[1]] == "-":
                    piece_to_move = None
                else:
                    piece_to_move = game.get_board()[coord_from[0]][coord_from[1]]
                if piece_to_move is not None:
                    mouse_drag(piece_to_move)

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_up = event
                # assign square_to
                square_to = format_to_let(mouse_up.pos[1] // 64, mouse_up.pos[0] // 64)
                # promotion prompt
                if piece_to_move is None:
                    break
                if game.get_turn() == "white":
                    if piece_to_move.get_color() == "white":
                        if piece_to_move.get_callsign() == "P":
                            if square_to[1] == '8':
                                promotion(piece_to_move)
                if game.get_turn() == "black":
                    if piece_to_move.get_color() == "black":
                        if piece_to_move.get_callsign() == "P":
                            if square_to[1] == '1':
                                promotion(piece_to_move)

                game.make_move(square_from, square_to)
                # if game.get_game_state() == "UNFINISHED":
                    # eval_move = engine.eval_move("black")
                    # game.make_move(eval_move[0], eval_move[1])


game_loop()
pygame.quit()
quit()