"""
This module contains all functions used for all board operations:
    1.  Creation
    2.  Updating
    3.  Winner checking
"""

from constants import BoardConstants, DisplayMessages
import copy



def correctBoard(board):
    """
    Returns True if board is an n X n list and all the items are either
      X , O or a string of ints in 1..n*n. Returns False otherwise.
    """
    length = len(board)
    unselected = []
    for i in range (length * length): # add all numbers representing all cells uin the grid
        unselected.append(str(i + 1))
    unselected = unselected + [BoardConstants.BOARD_ITEM_O,BoardConstants.BOARD_ITEM_X]

    for row in board:
         if len(row) != length:
             return False
         for item in row:
             if item not in unselected:
                 return False
    return True


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


def updateBoard(board, move, symbol):
    """
    Returns a new board with item at position move set to item 

    board : An n by n list of strings of the integers in 1..n*n
    move : An int in 1..n*n
    symbol: A character, either X or O
    """
    move = int(move)
    n = len(board)
    row = move // n    # Each row contains sorted ints in the range  1..n
    if move % n == 0 :
        row -= 1  
    col = (move + (n -1)) % n  # Each col i contains ints (i+1)+kn with k in 0..n-1
    new_board = copy.deepcopy(board)
    new_board[row][col] = symbol
    return new_board


def checkRowWin(board):
   """
   Returns a symbol X or O if that symbol has a winning row in board, else it returns None.
   """
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
    Returns the  symbol X or O, if that symbol wins along the diagonal starting at position start along
    gradient offset. Otherwise, returns None.

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


def checkDiagonals(board):
    """
    Returns the  symbol X or O, if that symbol wins along both diagonals in board. Otherwise, returns None.
    """
    main_diag = checkDiagional(board,(0,0),1)   #check diagonals
    second_diag = checkDiagional(board,(0,len(board)-1),-1)
    return [main_diag, second_diag] 


def checkDraw(board):
    draw = True
    for row in board:
        for item in row:
            if item != BoardConstants.BOARD_ITEM_O and item != BoardConstants.BOARD_ITEM_X:
                draw =  False 
    if draw:
        return DisplayMessages.PLAYERS_DRAW


def checkWin(board):
    """
    Returns a list of items each of which is None or a winning board symbol X or O.
    """
    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
    row_win = checkRowWin(board)     #check row win
    col_win = checkRowWin(transposed_board)      #check column win
    diags =  checkDiagonals(board)
    return [row_win, col_win]+diags

def hasPlayerWon(board,player):
    """
    Returns True if player has won the game in the given board, False otherwise

    Parameter player: Is either X or O
    """
    return player in checkWin(board)
           
def keepPlaying(board):
    """
    Returns True  and an empty string if the game is not over yet
    Otherwise, it returns False, plus a message on the game outcome, which can be one of three 
            1. Player X has won.
            2. PLayer O has won.
            3. The game as ended in a draw.
    """
    draw = checkDraw(board)     #check draw
    results = checkWin(board) + [draw]
    
    if BoardConstants.BOARD_ITEM_O in results: 
        return False, DisplayMessages.PLAYER_O_WINS
    elif BoardConstants.BOARD_ITEM_X in results:
        return False, DisplayMessages.PLAYER_X_WINS
    elif DisplayMessages.PLAYERS_DRAW in results:
        return False, DisplayMessages.PLAYERS_DRAW

    return True,""

