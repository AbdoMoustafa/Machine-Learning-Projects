from copy import deepcopy
import pygame

# RGB
from checkers import piece, board, constants, game, piece
from checkers.board import Board

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, max_player, game):
    # If game is still running, and we are at the last node, we get the evaluation of the position and return it,
    # along with the position itself.
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')  # Starting point
        best_move = None

        for move in get_all_moves(position, WHITE, game):
            # For every potential move we call minimax to evaluate
            evaluation = minimax(move, depth - 1, False, game)[0]

            maxEval = max(maxEval, evaluation)

            # If the current move yields the best score, we set it as best_move
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move



    else:
        minEval = float('inf')  # Starting point
        best_move = None

        for move in get_all_moves(position, RED, game):
            # For every potential move we call minimax to evaluate
            evaluation = minimax(move, depth - 1, True, game)[0]

            minEval = min(minEval, evaluation)

            # If the current move yields the best score, we set it as best_move
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


# Get all possible moves for a given position
def get_all_moves(board, color, game):
    moves = []  # Storing new board with newly moved piece

    # Loop through all pieces on the board a retrieve all valid moves
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # Deep copying board as we want to determine what the new board will look like after making a move
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col, )
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, temp_board, game, skip):
    board.move(piece, move[0], move[1])  # Splitting tuple

    # if we skipped over a piece
    if skip:
        board.remove(skip)
    return board
