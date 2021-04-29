"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
        self.starting_pos = True

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.starting_pos=False


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        available_moves = []
        cur_square=board.find_piece(self)
        cur_row=cur_square.row
        cur_col=cur_square.col

        move_direction = 1 if self.player == Player.WHITE else -1
        sq1 = Square.at(cur_row + move_direction, cur_col)
        if  board.square_empty(sq1):
            available_moves.append(sq1)
            if self.starting_pos:
                sq2 = Square.at(cur_row + (2*move_direction), cur_col )
                if  board.square_empty(sq2):
                    available_moves.append(sq2)
        
        return available_moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """
    def get_available_moves(self, board):

        available_moves = []
        cur_square=board.find_piece(self)
        cur_row=cur_square.row
        cur_col=cur_square.col

        knight_row=[-2, -1, 1, 2]
        knight_col=[1, 2, 2, 1]
        for x in range(0, len(knight_row) ):
            poss_row=cur_row+knight_row[x]
            poss_col=cur_col+knight_col[x]
            if poss_col>=0 and poss_col<8 and poss_row>=0 and poss_row<8:
                sq = Square.at(poss_row, poss_col)
                available_moves.append(sq)
            poss_row=cur_row-knight_row[x]
            poss_col=cur_col-knight_col[x]
            if poss_col>=0 and poss_col<8 and poss_row>=0 and poss_row<8:
                sq = Square.at(poss_row, poss_col)
                available_moves.append(sq)

        return available_moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """
    def get_available_moves(self, board):

        available_moves = []
        return available_moves


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []