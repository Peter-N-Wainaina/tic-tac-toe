"""
The controller class to run the  N tic-tac-toe gamegame 
"""
from board import Board
from player import Player,AIPlayer
from consts import *

class Game(object):
    """
    Represents a tictactoe game
    """
    #HIDDEN ATTRIBUTES
    #
    # Attribute _board: The game board
    # Invariant: _board is Board object
    #
    # Attribute _players: The players in the game 
    # Invariant: _players is a (possibly empty) list of Player Objects
    #
    # Attribute _winner : The symbol of the winner in the game
    # Invariant: _winner is either None(no winner), or the symbol of a player in
    #           _players
    #
    # Attribute _current: The index of the current player in _players
    # Inavriant: _current is an int in 0..len(_players) - 1

    def getBoard(self):
        """
        Returns the game baord
        """
        return self._board
    
    def getWinner(self):
        """
        Returns the winner of the game
        """
        return self._winner
    
    def getCurrentPlayer(self):
        """
        Returns the current player
        """
        return self._players[self._current]
    
    def getPlayers(self):
        """
        Returns the players in the game
        """
        return self._players
    
    def addPlayer(self,player):
        """
        Adds givem player to the game
        """
        assert isinstance(player,Player)
        self._players.append(player)

    def __init__(self,dim,streak=None):
        """
        Initializes the game with the given parameters
        """
        assert isinstance(dim,int) and dim>0
        assert streak is None or (isinstance(streak,int) and streak>0)

        self._board = Board(dim = dim , streak = streak)
        self._players = []
        self._winner =  None
        self._current = 0

    def printMessage(self, message, color = ""): 
        exit = "" if color == "" else ANSI_EXIT
        print(color + message + exit)


    def displayBoard(self):
        """
        Prints the board to terminal, formatting as necessary to represent
        a typical tictactoe board.
        """
        dim = self._board.getDimension()
        cell_width = len(str(dim * dim)) + 1

        for row in self._board.getBoard():
            padded_row = []
            for cell in row:
                if cell == "X":
                    c = ANSI_GREEN
                elif cell == "O":
                    c = ANSI_YELLOW
                else:
                    c = ""
                padded_row.append("{color}{:^{width}}{reset}".format(cell, color = c,\
                                    width=cell_width, reset=ANSI_EXIT))
            print(" | ".join(padded_row))
            print("-" * (dim * ROW_SEPARATOR_MULTIPLE))


    def _humanSymbol(self):
        """
        Returns the symbol the human chooses, either X or O
        """
        self.printMessage(SELECT_SYMBOL_MESSAGE,ANSI_CYAN) 
        h_symbol = ""
        done = False
        while not done:
            h_symbol = input().strip().upper()
            done = True if h_symbol in ["X","O"] else False
            if not done :
                self.printMessage(WRONG_SYMBOL_MESSAGE,ANSI_RED) 
        return h_symbol

    def _humanStarts(self):
        """
        Returns True if the human chooses to start, else False
        """
        done = False
        h_starts = False
        self.printMessage(WHO_STARTS_MESSAGE,ANSI_CYAN) 
        while not done:
            h_input = input().strip().upper()
            done = True if h_input in ["YES","NO"] else False
            if not done:
                self.printMessage(CHOOSE_YES_OR_NO,ANSI_RED)
            else:
                h_starts = True if h_input == "YES" else False
        return h_starts

    def startGame(self):
        """
        Starts the game by adding players, and updating the _players attribute to 
        determine which player starts
        """
        self.printMessage(WELCOME_MESSAGE,ANSI_MAGENTA)
        self.printMessage(NEW_LINE)
 
        h_symbol = self._humanSymbol()
        human_player = Player(h_symbol)
        ai_symbol = "X" if h_symbol != "X" else "O"
        ai_player = AIPlayer(ai_symbol)
        #Determine who starts 
        h_starts = self._humanStarts()
        self._players = [human_player,ai_player] if h_starts else \
                        [ai_player,human_player]
        self.run()

    def advance(self):
        """
        Moves to the next player
        """
        self._current = (self._current + 1) % len(self._players) 

    def run(self):
        keep_running = True
        while keep_running:
            #make move
            c_player = self.getCurrentPlayer()
            oppo = self._players[(self._current - 1) % len(self._players)]
            self.displayBoard()
            self.printMessage(NEW_LINE)
            move = c_player.chooseMove(self._board,oppo) 
            self._board.makeMove(c_player,move)
            message = c_player.getSymbol() + " chooses " + str(move[0] * \
                        self._board.getDimension() + move[1] + 1)
            self.printMessage(message,ANSI_CYAN)

            #eval move
            p_won = self._board.hasWon(c_player)
            b_full = self._board.isBoardFull()
            keep_running = not (b_full or p_won) #Demorgan's

            #advance or end game
            if keep_running:
                self.advance()
            else:
                self.displayBoard()
                if p_won:
                    self._winner = c_player
                self.endGame()

    def endGame(self):
        if self._winner is None:
            self.printMessage(DRAW_MESSAGE,ANSI_MAGENTA)
        else:
            message = "Player " + self._winner.getSymbol() + \
                      " wins"
            self.printMessage(message,ANSI_MAGENTA)
        