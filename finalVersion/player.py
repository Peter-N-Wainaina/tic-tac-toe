"""
The classes in this module model  tictactoe players.
"""
from  board import Board, isValidPosition
from random import randint
from consts import *

class Player(object):
    """
    Represents a human player 
    """
    #HIDDEN ATTRIBUTES
    #
    #Attribute _symbol: The player's symbol
    #Invariant: _symbol is a single uppercase character
    
    def getSymbol(self):
        """
        Returns the player symbol
        """
        return self._symbol
    
    def __init__(self,symbol):
        """
        Initializes a player with the given symbol, capitalized if necessary
        """
        assert isinstance(symbol,str) and len(symbol) == 1
        self._symbol = symbol.upper()

    def convertMove(self,b,move):
        """
        Converts the player's chosen move to an (int, int) tuple of 
        the index in the game board.

        Parameter b: The game board 
        Precondition: b is a board object

        Parameter move: The player's chosen move 
        Precondition: move is a valid position in board
        """
        assert isinstance(b,Board) 
        assert isinstance(move,int) and isValidPosition(b.getDimension(),move)

        dim = b.getDimension()
        row = move // dim    # Each row contains sorted ints in the range  1..n
        if move % dim == 0 :
            row -= 1  
        col = (move + (dim -1)) % dim
        return (row,col)

    def chooseMove(self,board,oppo):
        """
        Returns an (int,int) tuple of the move the human player has chosen.

        Gets a valid terminal input from the user, and int indicating the position
        they want to move to, and converts this to the indices on the board. For 
        example, 5 in a 3 by 3 board should be (1,1). Note that the move must be 
        an empty position on the board. 
        """
        assert isinstance(board,Board)
        dim = board.getDimension()
        moves = board.possibleMoves()
        done = False
        while not done:
            move = input(SELECT_MOVE_MESSAGE).strip()
            try:
                move = int(move)
                row = move // dim    # Each row contains sorted ints in the range  1..n
                if move % dim == 0 :
                    row -= 1  
                col = (move + (dim -1)) % dim
                if (row,col) in moves:
                    done = True
                    return (row,col)
                else:
                    raise MoveUnavailableError
            except ValueError:
                print(INVALID_TYPE_ERROR)
            except MoveUnavailableError:
                print(UNAVAILABLE_MOVE) 


class AIPlayer(Player):
    """
    Represents the AI player and uses minimax to choose the best move
    """

    def _evaluateMove(self,board,move,opponent,isMaxPlayer,depth):
        """
        Evaluates the move on board from the perspective of this AIPlayer

        Parameters:
        move: An (int, int) tuple representing the move's position on the board.
        player: The current player making the move.
        opponent: The opponent player.
        isMaxPlayer: A boolean indicating if the current evaluation is for the maximizing player.
        depth: The depth of the move in the game tree.

        Returns: An integer score representing the value of the move."""
        assert isinstance(board,Board)

        player = self if isMaxPlayer else opponent
        board.makeMove(player,move)
        if board.hasWon(player):
            board.undoMove(move)
            return WIN - depth if isMaxPlayer else LOSS + depth
        
        if board.isBoardFull():
            board.undoMove(move)
            return DRAW - depth if isMaxPlayer else DRAW + depth

        scores = []
        moves = board.possibleMoves()
        for next_move in moves:
            scores.append(self._evaluateMove(board,next_move, opponent,\
                                             not isMaxPlayer, depth + 1))
            #board.undoMove(move)
        board.undoMove(move)

        return min(scores) if isMaxPlayer else max(scores)    

    def _scoreMoves(self,moves,opponent,board):
        """
        Returns an (int,int):int dictionary of the moves and their corresponding 
        scores.
        """
        scores = {}
        for move in moves:
            scores[move] = self._evaluateMove(board,move,opponent,True,0)
        return scores
    
    def _getRandom(self,items):
        """
        Returns one of the item in items at random
        """

        index = randint(0,len(items) - 1)
        return items[index]

    def _getBestMove(self,scores,board):
        """
        Returns one of the highest value moves. 

        Parameter moves: The possible moves and their corresponding scores
        Precondition: moves is an (int,int):int dictionary
        """
        assert isinstance(board,Board)
        max_scores = [move for move,score in scores.items() \
                     if score == max(scores.values())]    #get highest scores
        centers = board.getCenterPieces()
        high_centers = [center for center in centers if center in max_scores ]
        return self._getRandom(high_centers) if high_centers != [] else\
                self._getRandom(max_scores)

    def chooseMove(self,board,opponent):
        """
        Returns an (int,int) tuple, the best move from the perspective of this AI
        player.Opponent is a player object.
        """
        assert isinstance(board,Board)
        assert isinstance(opponent,Player)

        pos_moves = board.possibleMoves()
        scores = self._scoreMoves(pos_moves,opponent,board)
        return self._getBestMove(scores,board)


class MoveUnavailableError(Exception):
    """
    Error raised when Player chooses a move that is unavailable
    """
