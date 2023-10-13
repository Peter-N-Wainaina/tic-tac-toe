"""
Given an n by n list, this module prints it in a grid format, 
formatting it to resemble a tic-tac-toe board
"""

import constants 

def correctBoard(board):
    """
    Returns True if list is an n X n list and all the items are either
      X , O or a string of ints in 1..n*n. Returns False otherwise.
    """
    length = len(board)
    unselected = []
    for i in range (length * length): # add all numbers representing all cells uin the grid
        unselected.append(str(i + 1))
    unselected = unselected + [constants.BOARD_ITEM_O,constants.BOARD_ITEM_X]

    for row in board:
         if len(row) != length:
             return False
         for item in row:
             if item not in unselected:
                 print(board)
                 print(unselected)
                 print(item)
                 return False
    return True



def displayBoard(board): #TODO: Make it more robust for large n, currently hard-coded to support 3 by 3 board
    """
    Prints the given n by n board in the tic-tac-toe board format. 
    board : An n by n list whose items are either X or O  or a string in 1.. n * n   
    """
    assert correctBoard(board),\
        repr("The board provided  is not valid")
    
    row_dash  = constants.ROW_SEPARATOR * constants.ROW_SEPARATOR_LENGTH
    n = len(board)
    for row in range(n):
        row_data = ""
        for col in range(n):
            if col == 0:  # for formatting first column
                row_data += " "
            item = board[row][col]

            if item == constants.BOARD_ITEM_X:
                item =  constants.ANSI_GREEN + item 
            elif item == constants.BOARD_ITEM_O:
                item =  constants.ANSI_MAGENTA + item
            row_data += item + constants.ANSI_EXIT + constants.ANSI_BOLD + constants.ANSI_EXIT
       
            if col < n-1 :
                row_data += constants.COLUMN_SEPARTOR
        print(row_data)
        if row < n-1:
            print(row_dash)


