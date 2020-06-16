from Chess import ChessGame, Piece, King, Queen, Rook, Bishop, Knight, Pawn, format_to_nums, format_to_let
from Engine import Engine

game = ChessGame()
newGame = ChessGame()


engine = Engine(game)

game.make_move("a2", "a3")
game.make_move("f7", "f5")
game.make_move("d2", "d4")
game.make_move("b8", "c6")

print(engine.eval_move("black"))

