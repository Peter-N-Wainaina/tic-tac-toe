import boardLogic as boardLogic
from constants import AnsiCodes, DisplayMessages,\
    BoardConstants, SpaceFormatters
import randomMove
import heuristics
import proofOfConcept



def displayBoard(board): #TODO: Make it more robust for large n, currently hard-coded to support 3 by 3 board
    """
    Prints the given n by n board in the tic-tac-toe board format. 
    board : An n by n list whose items are either X or O  or a string in 1.. n * n   
    """
    print(board)
    assert boardLogic.correctBoard(board),\
        repr("The board provided  is not valid")
    
    row_dash  = BoardConstants.ROW_SEPARATOR * BoardConstants.ROW_SEPARATOR_LENGTH
    n = len(board)
    for row in range(n):
        row_data = ""
        for col in range(n):
            if col == 0:  # for formatting first column
                row_data += " "
            item = board[row][col]

            if item == BoardConstants.BOARD_ITEM_X:
                item =  AnsiCodes.ANSI_GREEN + item 
            elif item ==BoardConstants.BOARD_ITEM_O:
                item =  AnsiCodes.ANSI_MAGENTA + item
            row_data += item + AnsiCodes.ANSI_EXIT + AnsiCodes.ANSI_BOLD + AnsiCodes.ANSI_EXIT
       
            if col < n-1 :
                row_data += BoardConstants.COLUMN_SEPARTOR
        printFormattedMessage(row_data)
        if row < n-1:
            printFormattedMessage(row_dash)


def printFormattedMessage(message, color = ""):
    if color == "":
        exit = ""
    else:
        exit = AnsiCodes.ANSI_EXIT
    print(color+ message + exit)


def getPlayerMove(unselected):
    """
    Returns a selected valid player move as an int, and removes
    the selected move from unselected. It also returns this modifies unselected. 

    A valid move is any item  in unselected

    unselected: A list of strings of the numbers 1...9
    """
    move = input( DisplayMessages.SELECT_MOVE_MESSAGE).strip()
    while move not in unselected :
        printFormattedMessage( DisplayMessages.INVALID_INPUT_ERROR, AnsiCodes.ANSI_RED)
        move = input( DisplayMessages.SELECT_MOVE_MESSAGE).strip()
    unselected.remove(move)
    return int(move), unselected 


def getPlayingSymbols():
    """
    Returns a tuple of valid symbols, one that the player would like to use
    and the other that the computer will use. A valid symbol is either X or O

    Example, if the player selectes X, return value is ("X,"O) else ("O,"X).

    """ 
    symbol = input( DisplayMessages.SELECT_SYMBOL_MESSAGE).strip().upper()
    while symbol not in [BoardConstants.BOARD_ITEM_O,BoardConstants.BOARD_ITEM_X]:
        printFormattedMessage( DisplayMessages.INVALID_INPUT_ERROR,AnsiCodes.ANSI_RED)
        symbol = input( DisplayMessages.SELECT_SYMBOL_MESSAGE).strip().upper()

    if symbol == BoardConstants.BOARD_ITEM_X:
        result = (BoardConstants.BOARD_ITEM_X,BoardConstants.BOARD_ITEM_O)
    else:
        result =  (BoardConstants.BOARD_ITEM_O,BoardConstants.BOARD_ITEM_X)
    printFormattedMessage(SpaceFormatters.NEW_LINE)
    return result


def stopPlaying(board): #TODO: A lot going on here, refactor? 
    printFormattedMessage(SpaceFormatters.NEW_LINE)
    #displayBoard(board)
    printFormattedMessage(SpaceFormatters.NEW_LINE)
    if  not boardLogic.keepPlaying(board)[0]:
        printFormattedMessage( AnsiCodes.ANSI_BLINK + boardLogic.keepPlaying(board)[1], AnsiCodes.ANSI_YELLOW) #TODO: Print specific message about winner i.e I win or you win
        return True


def runGame():
    printFormattedMessage( DisplayMessages.WELCOME_MESSAGE,AnsiCodes.ANSI_CYAN)
    printFormattedMessage(SpaceFormatters.NEW_LINE)

    player_symbol, computer_symbol = getPlayingSymbols() 
    board = boardLogic.createBoard(BoardConstants.BOARD_SIZE) #TODO: Hard code to 3 by 3 matrix, but maybe ask user for choice, also for unselected
    unselected = boardLogic.initialUnselected(BoardConstants.BOARD_SIZE) 
    printFormattedMessage(SpaceFormatters.NEW_LINE)

    ai_starts = False
    if not ai_starts:
        while boardLogic.keepPlaying(board)[0]:
            move = proofOfConcept.getTestingMove(board,computer_symbol,player_symbol,unselected)
            unselected.remove(move)
            board = boardLogic.updateBoard(board, move, computer_symbol)
            printFormattedMessage(f"I choose {move}, your turn" , AnsiCodes.ANSI_CYAN)
            displayBoard(board)

            if stopPlaying(board):
                break

            move, unselected = getPlayerMove(unselected) # initially all positions are unselected
            board = boardLogic.updateBoard(board, move, player_symbol) 

            #move, unselected = randomMove.pickRandomMove(unselected) #TODO: Make player choose computer strength 
            #move, unselected  = heuristics.pickHeuristicMove(board, unselected, computer_symbol)
            #print("unselected",unselected)
            #print("move",move)
            # unselected.remove(move)
            # board = boardLogic.updateBoard(board, move, computer_symbol)
            # printFormattedMessage(f"I choose {move}, your turn" , AnsiCodes.ANSI_CYAN)
            if  stopPlaying(board):
                break


if __name__ == '__main__':
    runGame()
