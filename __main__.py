import display
import constants
import boardLogic
from moveGenerator import randomMove



def printError(message):
    print(constants.ANSI_RED + message + constants.ANSI_EXIT)


def getPlayerMove(unselected):
    """
    Returns a selected valid player move as an int, and removes
    the selected move from unselected. It also returns this modifies unselected. 

    A valid move is any item  in unselected

    unselected: A list of strings of the numbers 1...9
    """
    move = input(constants.SELECT_MOVE_MESSAGE)
    while move not in unselected :
        printError(constants.INVALID_INPUT_ERROR)
        move = input(constants.SELECT_MOVE_MESSAGE)
    unselected.remove(move)
    return int(move), unselected 


def stopPlaying(board):
    print(constants.NEW_LINE)
    display.displayBoard(board)
    print(constants.NEW_LINE)
    if  not boardLogic.keepPlaying(board)[0]:
        print(constants.ANSI_YELLOW + constants.ANSI_BLINK + boardLogic.keepPlaying(board)[1]  + constants.ANSI_EXIT)
        return True


def runGame():
    board = boardLogic.createBoard(3) #TODO: Hard code to 3 by 3 matrix, but maybe ask user for choice, also for unselected
    unselected = boardLogic.initialUnselected(3) 
    display.displayBoard(board)

    while boardLogic.keepPlaying(board)[0]:
        move, unselected = getPlayerMove(unselected) # initially all positions are unselected
        board = boardLogic.updateBoard(board, move, constants.BOARD_ITEM_X) #TODO: Hard code item x, but have player choose X or O eventuslly
        if stopPlaying(board):
            break
        move, unselected = randomMove.pickComputerMove(unselected)
        board = boardLogic.updateBoard(board, move, constants.BOARD_ITEM_O)
        print(constants.ANSI_CYAN + f"I choose {move}, your turn" + constants.ANSI_EXIT)
        if  stopPlaying(board):
            break



if __name__ == '__main__':
    runGame()
