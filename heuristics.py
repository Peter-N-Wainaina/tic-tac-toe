"""
Picks a move from the unselected list by following this set of provided heuristics
    1. If there is a winning move, take it. 
    2. If your opponent is about to win, block them. 
    3. Take middle position if possible.
    4. Take corner positions over edge positions.
"""
import boardLogic
from constants import BoardConstants
import random


def pickHeuristicMove(board, unselected, symbol):
    #TODO:assert preconditions
    computer_symbol = symbol
    if computer_symbol == BoardConstants.BOARD_ITEM_X:
        player_symbol = BoardConstants.BOARD_ITEM_O
    else:
        player_symbol = BoardConstants.BOARD_ITEM_X
    board_size = len(board)

    comp_win = checkWinningMove(board, unselected, computer_symbol)
    oppo_win = checkWinningMove(board, unselected, player_symbol )
    middle = checkMiddle(unselected, board_size)
    corner = checkCorner(unselected, board_size )
    edge = pickRandom(unselected) #otherwise only edge moves left, pick random

    all_moves = [comp_win, oppo_win, middle, corner, edge] #Note that order matters
    for move in all_moves:
        if move!=None:
            unselected.remove(str(move))
            return int(move), unselected


def checkWinningMove(board, unselected, symbol):
    """
    Returns a valid winning move in board for symbol if it exists, 
    otherwise returns None

    board : An n by n list of a valid tic-tac-toe board with
            at least one move left to win
    unselected : A list of string of all ints in board
    symbol : Either X or O
    """
    for pos in unselected:
        int_pos = int(pos)
        new_board =  boardLogic.updateBoard(board, int_pos, symbol)
        possible_wins = boardLogic.checkWin(new_board)
        possibles = []
        for possible in possible_wins:
            if possible != None :
                possibles.append(int_pos)
        move = pickRandom(possibles)
        if move != None:
            return move
            

def checkMiddle(unselected, board_size):
    """
    Returns an int, the position of a middle square of an n by n board that is unselected
    For odd board_size, only one such square exists, else check the middle 2 by 2 square.

    unselected : A list of string of ints
    board_size : An int > 0 
    """
    assert type(board_size) == int , "Board size must be an int"
    assert board_size > 0, "Board size must be greater than 0"

    half = board_size // 2
    if board_size % 2 != 0 :  #odd
        squares = [((board_size * half) + half + 1)]
    else:   #even 
        top_left = (board_size * (half -1)) + half
        bottom_left = top_left + board_size
        squares = [ top_left , top_left + 1, bottom_left, bottom_left + 1]
    possible_middle = []
    for square in squares:
        if str(square) in unselected:
            possible_middle.append(square)
    return  pickRandom(possible_middle)
    

def checkCorner(unselected, board_size):
    """
    Returns an int, the position of a corner square of an n by n board that is unselected

    unselected : A list of string of ints
    board_size : An int > 0 
    """
    diff = board_size - 1
    top_left = 1
    bottom_right = board_size * board_size
    corners =  [top_left, top_left + diff, bottom_right - diff , bottom_right]
    possible_corners = []
    for corner in corners:
        if str(corner) in unselected:
            possible_corners.append (corner)
    return pickRandom(possible_corners)

def pickRandom(unselected):
    if len(unselected) != 0:
        move_index = random.randint(0,len(unselected)-1)
        return int(unselected[move_index])