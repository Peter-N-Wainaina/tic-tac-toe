"""
This module contains all functions used for all board operations:
    1.  Creation
    2.  Updating
    3.  Winner checking
"""

import constants

def createBoard(n):
    """
    Returns an n by n list of ints in 1 .. n * n, where each row i
        is a sorted list of ints in the range [((n * i) + 1) .. (n * (i + 1))]
    Example : createBoard(3) is [[1,2,3],[4,5,6],[7,8,9]]
    """
    board = []
    item = 1
    for _ in range(n):
        row_data = []
        for _ in range(n):
            row_data.append(str(item))
            item += 1
        board.append(row_data)
    return board 


def initialUnselected(n):
    """
    Returns a list of strings of all ints in range 1..n*n
    """
    unselected = []
    i = 1
    while i < n*n + 1:
        unselected.append(str(i))
        i += 1
    return unselected


def updateBoard(board, move, cell_data):
    """
    Returns a new board with item at position move set to item 

    board : An n by n list of strings of the integers in 1..n*n
    move : An int in 1..n*n
    cell_data: A character, either X or O
    """
    n = len(board)
    row = move // n    # Each row contains sorted ints in the range  1..n
    if move % n == 0 :
        row -= 1  
    col = (move + (n -1)) % n  # Each col i contains ints (i+1)+kn with k in 0..n-1
    board[row][col] = cell_data 
    return board


def checkRowWin(board):
   for row in board:
        row_data = row[0]
        row_win = True
        for item in row:
           if item != row_data:
               row_win = False
        if row_win:
            return row_data
        
        
def checkDiagional(board,start, offset):
    """
    Returns the  element at position board[start[0]][start[1]] if all the elements along 
    diagonal starting at position start along gradient -offset

    Example: For a 3 by 3 board, with start (0,0) and offset 1, we check the diagonal [(0,0),(1,1),(2,2)]
    """ 
    row_i =  start[0]
    col_i = start[1]  
    item = board[row_i][col_i]
    diag_win = True
    for i in range(len(board)-1):
        row_i += 1
        col_i += offset
        if board[row_i][col_i] != item:
            diag_win = False
    if diag_win:
        return item

           
def keepPlaying(board):
    """
    Returns True  and an empty string if the game is not over yet
    Otherwise, it returns False, plus a message on the game outcome, which can be one of three 
            1. Player X has won.
            2. PLayer O has won.
            3. The game as ended in a draw.
    """

    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
    row_win = checkRowWin(board)     #check row win
    col_win = checkRowWin(transposed_board)      #check column win
    #check diagonals
    main_diag = checkDiagional(board,(0,0),1)
    second_diag = checkDiagional(board,(0,len(board)-1),-1)

    if row_win == constants.BOARD_ITEM_O or col_win == constants.BOARD_ITEM_O or \
        main_diag  == constants.BOARD_ITEM_O or second_diag == constants.BOARD_ITEM_O: 
        return False, constants.PLAYER_O_WINS
    elif row_win == constants.BOARD_ITEM_X or col_win == constants.BOARD_ITEM_X or \
        main_diag == constants.BOARD_ITEM_X or second_diag == constants.BOARD_ITEM_X:
        return False, constants.PLAYER_X_WINS
    #check draw
    draw = True
    for row in board:
        for item in row:
            if item != constants.BOARD_ITEM_O and item != constants.BOARD_ITEM_X:
                draw =  False 
    if draw:
        return False, constants.PLAYERS_DRAW

    return True,""

