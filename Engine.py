from Chess import ChessGame, Piece, King, Queen, Rook, Bishop, Knight, Pawn, format_to_nums, format_to_let


class Engine:
    def __init__(self, game):
        self.game = game

    def get_all_moves(self):
        all_moves = set()
        for piece in self.game.get_piece_list():
            if piece.get_color() == "black":
                for move in piece.get_move_set():
                    all_moves.add((format_to_let(piece.get_rank(), piece.get_file()), move))
        return all_moves

    def evaluate(self):
        score = 0
        for piece in self.game.get_piece_list():
            if piece.get_color() == "white":
                score += piece._strength
            if piece.get_color() == "black":
                score -= piece._strength
        return score

    def eval_move(self):
        reverted_piece_list = self.game.get_piece_list().copy()
        reverted_cap_list = self.game.get_captured_list().copy()
        reverted_master_move_set_dict = dict()
        for piece in self.game.get_piece_list():
            reverted_master_move_set_dict.update({piece: piece.get_move_set().copy()})
        for piece in self.game.get_piece_list():
            if piece.get_color() == "black":
                from_rank = piece.get_rank()
                from_file = piece.get_file()
                current_position = format_to_let(piece.get_rank(), piece.get_file())
                for potential_move in piece.get_move_set():
                    self.game.test_move(current_position, potential_move)
                    self.game.print_board()
                    print(self.evaluate())
                    self.game.test_move(potential_move, current_position)
                    self.game.set_piece_list(reverted_piece_list)
                    self.game.set_captured_list(reverted_cap_list)




