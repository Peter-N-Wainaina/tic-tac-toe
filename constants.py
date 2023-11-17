#Board 
class BoardConstants():
    ROW_SEPARATOR_LENGTH = 11  #TODO: Make this vary with board length
    ROW_SEPARATOR = "-"
    COLUMN_SEPARTOR = " | "  # note the spaces before and after |
    BOARD_ITEM_X = "X"
    BOARD_ITEM_O = "O"
    BOARD_SIZE = 3


class SpaceFormatters():
    NEW_LINE = "\n"
    TAB = "\t"


class DisplayMessages():
    SELECT_MOVE_MESSAGE = "Choose position from one of the numbers: "
    INVALID_INPUT_ERROR = "Please enter a valid input!"
    SELECT_SYMBOL_MESSAGE = "Would you like to be X or O?"
    WELCOME_MESSAGE = "Welcome, let's play some TicTacToe :)"
    PLAYER_X_WINS = "Player X Wins"
    PLAYER_O_WINS = "Player O Wins"
    PLAYERS_DRAW = "We draw :)"


#Ansi codes
class AnsiCodes():
    ANSI_OPEN_CODE = "\033["
    ANSI_M = "m"
    ANSI_EXIT = ANSI_OPEN_CODE + "0" + ANSI_M
    ANSI_BOLD = ANSI_OPEN_CODE + "1" + ANSI_M
    ANSI_GREEN =  ANSI_OPEN_CODE + "32" + ANSI_M
    ANSI_YELLOW=  ANSI_OPEN_CODE + "33" + ANSI_M
    ANSI_RED=  ANSI_OPEN_CODE + "31" + ANSI_M
    ANSI_MAGENTA=  ANSI_OPEN_CODE + "35" + ANSI_M
    ANSI_CYAN=  ANSI_OPEN_CODE + "36" + ANSI_M
    ANSI_BLINK = ANSI_OPEN_CODE + "5" + ANSI_M