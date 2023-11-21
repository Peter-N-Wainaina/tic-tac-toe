"""
This class represents the playing board
"""
import player

class Board(object):
    """
    Represents the tictactoe board
    """
    #HIDDEN ATTRIBUTES
    #
    #Attribute _dimension: The dimension of the board
    #Invariant: _dimension is an int > 0 
    #
    #Attribute _board: A 2D N by N list           
    #Invariant: _board is an N by N list of strings that are either containing 
    #           the player's symbols or valid positions. Valid positions are strings of 
    #           ints in range 1 .. N*N inclusive
    #  
    #Attribute _moves: The moves already made in the game
    #Invariant: _moves is a list of (int,int) tuples, the indices of the made moves
    #            in the board. It's length is equal to the occurences of the player
    #            symbols on _board
    #Attribute _streak: The number of consecutive similar symbols required to win
    #Invariant: _ streak is an int > 0


    def getDimension(self):
        """
        Returns board dimension.
        """
        return self._dimension
    
    def getBoard(self):
        """
        Returns the game board
        """
        return self._board
    
    def getMoves(self):
        """
        Returns the moves made in the gamne thus far
        """
        return self._moves

    def __init__(self,dim,moves = None,board = None,streak=None):
        """
        Initializes the game board with the given parameters
        """
        assert isinstance(dim, int) and dim > 0 
        if board is not None :
            assert  isValidBoard(board,dim) and isValidMadeMoves(board,moves)
         #TODO: Assert that the moves are correctly filled in the board?

        self._dimension = dim
        self._moves = [] if moves is None else moves
        self._streak = self._dimension if streak is None else streak
        self._board = self._createEmptyBoard(self._dimension) if board is None\
                        else board

    def _getPosition(self,r,c):
        """
        Returns the valid position at the given row and column.
        A valid position
        """
        return str(r * self._dimension + c + 1)
    
    def _createEmptyBoard(self,dim):
        """
        Returns an empty board of dimensions dim, initialised with valid board
        positions
        """
        board = []
        for r in range(dim):
            row = []
            for c in range(dim):
                pos = self._getPosition(r,c)
                row.append(pos)
            board.append(row)
        return board

    def clear(self):
        """
        Replaces all symbols placed in the board with valid positions
        """
        self._moves = []
        self._board = self._createEmptyBoard(self._dimension)

    def makeMove(self,p,move):
        """
        Places the player's symbol on the board at the position specified by move

        Precondition: move is a valid move on the board
        """
        assert isinstance(p,player.Player)
        r,c = move[0],move[1]
        self._board[r][c] = p.getSymbol()
        self._moves.append(move)

    def undoMove(self,move):
        """
        Removes the symbol at the position specified by move and replaces it 
        with its corresponding position
        """
        r,c = move[0],move[1]
        self._board[r][c] = self._getPosition(r,c)
        self._moves.remove(move)

    def possibleMoves(self):
        """
        Returns a list of (int,int) tuples of all possible moves left on the board
        """
        moves = []
        for r in range(self._dimension):
            for c in range(self._dimension):
                try:
                    int(self._board[r][c])
                    moves.append((r,c))
                except ValueError:
                    pass
        return moves
    
    def isBoardFull(self):
        """
        Returns True if the game board is full
        """
        return self.possibleMoves() == []

    def _diagonalStreak(self,p,streak = None):
        """
        Returns True if player p has a diagonal run of length streak.Streak is 
        self._streak if streak is None.
        """
        assert streak is None or (isinstance(streak,int) and streak>0)
        assert isinstance(p,player.Player)

        symbol = p.getSymbol()
        count1 = 0
        count2 = 0
        for i in range(self._streak):       
            if self._board[i][i] == symbol:   #primary diag
                count1 += 1
            else:
                count1 = 0
            
            if self._board[i][self._dimension-i-1] == symbol: # second diag
                count2 += 1
            else:
                count2 = 0
        return max(count1,count2) >= streak

    def _verticalStreak(self,p,streak = None):
        """
        Returns True if player p has a vertical run of length streak.
        """
        assert streak is None or (isinstance(streak,int) and streak>0)
        assert isinstance(p,player.Player)

        symbol = p.getSymbol()
        for col in range(self._dimension):
            count = 0
            for row in range(self._dimension):
                if self._board[row][col] == symbol:
                    count += 1
                else:
                    count = 0
            if count == streak:
                return True
        return False

    def _horizontalStreak(self,p,streak = None):
        """
        Returns True if player p has a horizontal run of length streak. 
        Parameter p is a Player object
        """
        assert streak is None or (isinstance(streak,int) and streak>0)
        assert isinstance(p,player.Player)

        symbol = p.getSymbol()
        for row in self._board:
            count = 0
            for item in row:
                if item == symbol:
                    count += 1
                else:
                    count = 0
            if count == streak:
                return True
        return False

    def hasWon(self,p,streak = None):
        """
        Returns True if player p has a run of length streak in this board, either 
        horizontally, vertically or diagonally
        """
        assert streak is None or (isinstance(streak,int) and streak>0)
        streak = self._dimension if streak is None else streak
        return self._diagonalStreak(p,streak) or \
            self._verticalStreak(p,streak) or \
            self._horizontalStreak(p,streak)
    
    def getCenterPieces(self): 
        """
        Returns a list of the center pieces on the move
        If board dimension is odd, this is one simply one cell in the middle, 
        otherwise return the cells in the middle 2 by 2 square
        """
        dim = self._dimension
        center_row = dim // 2
        center_col = dim // 2 
        if dim % 2 == 1: #ODD
            return [(center_row,center_col)]
        else:#EVEN
            bottom_right = (center_row,center_col)
            top_left = (center_row - 1, center_col - 1)
            top_right = (center_row - 1,center_col)
            bottom_left = (center_row,center_col - 1)
            return [bottom_left,bottom_right,top_left,top_right]


### Helper Functions ###
def isValidBoard(board,dim):
    """
    Returns True if board is a valid board i.e is a dim by dim list of strings.
    These strings are either 1 character player symbols or valid positions 
    """
    if len(board) != dim:
        return False
        
    for row in board:
        if len(row) != dim:
            return False
        for item in row:
            if  not(isinstance(item,str) and len(item) == 1 and  item.isupper()) \
                and not  isValidPosition(dim,int(item)):
                return False
    return True 

def isValidPosition(dim, pos):
    """
    Returns True if pos is a valid position in the board, otherwise False. 
    A valid position is an int in range 1 .. dim*dim
    Precondition: pos is an int
    """
    return pos >= 1 and pos <= dim*dim 

def isValidMadeMoves(board,moves):
    """
    Returns True if moves is a list of (int,int) tuples of moves made in board
    Precondition: board is a valid board
    """
    if moves == None: 
        return True
    collect_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col].isupper(): #ints don't have case
                collect_moves.append((row,col))
    return sorted(moves) == sorted(collect_moves)

