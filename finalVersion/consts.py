#   AI Player constants
WIN = 10
DRAW = 0
LOSS = -10

#Game constants
SELECT_MOVE_MESSAGE = "Choose Move:"
INVALID_TYPE_ERROR = "Move must be an integer."
UNAVAILABLE_MOVE = "Please select a move from those on display."
NEW_LINE  = "\n"
SPACE = " "
ROW_SEPARATOR_MULTIPLE = 4
WELCOME_MESSAGE = "Welcome, let's play some TicTacToe :)"
SELECT_SYMBOL_MESSAGE = "Would you like to be X or O?"
WRONG_SYMBOL_MESSAGE = "Please select X or O."
NEW_LINE = "\n"
TAB = "\t"
WHO_STARTS_MESSAGE = "Would you like to go first?"
CHOOSE_YES_OR_NO = "Please select yes or no."
DRAW_MESSAGE = "Not bad, we draw!"


#Ansi Codes
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