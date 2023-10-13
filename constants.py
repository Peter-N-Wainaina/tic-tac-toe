#Board 
ROW_SEPARATOR_LENGTH = 11
ROW_SEPARATOR = "-"
COLUMN_SEPARTOR = " | "  # note the spaces before and after |
BOARD_ITEM_X = "X"
BOARD_ITEM_O = "O"
PLAYER_X_WINS = "Player X Wins"
PLAYER_O_WINS = "Player O Wins"
PLAYERS_DRAW = "We draw :)"

#Ansi codes
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

#Display Message 
SELECT_MOVE_MESSAGE = "Choose position from one of the numbers: "
INVALID_INPUT_ERROR = "Please enter a valid input!"
NEW_LINE = "\n"
