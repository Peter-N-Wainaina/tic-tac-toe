import boardLogic
import copy
import random 

X = "X"
O = "O"
# board = [[X,2,X],[O,O,6],
#     [7,8,9]]
# moves = [(0,1),(1,2),(2,0),(2,1),(2,2)]
WIN = 10
LOSE = -10
DRAW = 0
players = [X,O]
class Board():
    def __init__(self,board = [[1,2,3],[4,5,6],[7,8,9]]):
        self.board = board
        self.board_dim = len(board)
        self.moves_made = []


    def horizontalWin(self,player): # returns player who has won, or None
        """
        Returns True if this player has a winning position in this board
        """
        size = self.board_dim
        for row in range(size):
            win = True
            for col in range(size):
                if self.board[row][col] != player:
                    win = False
            if win: 
                return True
        return False

    def verticalWin(self,player):
        size = self.board_dim
        for col in range(size):
            win = True
            for row in range(size):
                if self.board[row][col] != player:
                    win = False
            if win: 
                return True
        return False

    def diagonalWin(self,player):
        board = self.board
        main = board[0][0] == board[1][1] == board[2][2] == player
        second = board[0][2] == board[1][1] == board[2][0] == player
        return main or second

    def checkWin (self,player):
        return self.horizontalWin(player) or self.verticalWin(player)\
        or self.diagonalWin(player)

    def placePiece(self,move,player):
        r,c = move[0], move[1]
        self.board[r][c] = player

    def removePiece(self,move):
        #self.moves_made.remove(move)
        r,c = move[0], move[1]
        self.board[r][c] = str((r*3)+ (c+1))

    def possibleMoves(self):
        """
        Returns a list of all possible moves in board. A move is possible in
        any cell that contains an int

        Parameter board: An N by N list representing a tic-tac-toe board
        """
        size = self.board_dim
        moves = []
        for row in range(size):
            for col in range(size):
                if self.board[row][col] not in players:
                    moves.append((row,col))
        return moves

    def gameDraw(self):
        """
        Returns True if the board is full i.e there are no possible moves
        """
        return len(self.possibleMoves()) == 0
    
    def evaluateMove(self, move, player, opponent, isMaximizingPlayer, depth):
        """
        Evaluates the score of a move in a Tic-Tac-Toe game.

        Parameters:
        move: An (int, int) tuple representing the move's position on the board.
        player: The current player making the move.
        opponent: The opponent player.
        isMaximizingPlayer: A boolean indicating if the current evaluation is for the maximizing player.
        depth: The depth of the move in the game tree.

        Returns:
        An integer score representing the value of the move.
        """
        self.placePiece(move, player)
        if self.checkWin(player):
            #print(f"{player} wins with {self.board} and depth {depth} at move {move}")
            self.removePiece(move)
            return WIN - depth if isMaximizingPlayer else LOSE + depth
        #depth += 1 #  TODO: We have made one move, so we increase depth?
        if self.gameDraw():
            #print(f"Draw at move {move}")
            self.removePiece(move)
            return DRAW - depth if isMaximizingPlayer else DRAW + depth

        scores = []
        moves = self.possibleMoves()
        for next_move in moves:
            #print(f"{opponent} {not isMaximizingPlayer} with moves {moves} and current {next_move} and scores {scores}")
            scores.append(self.evaluateMove(next_move, opponent, player, not isMaximizingPlayer, depth + 1))
            #print(f"{opponent} {not isMaximizingPlayer} new scores {scores}")
            self.removePiece(next_move)
        self.removePiece(move)
        #print(f"{player} {isMaximizingPlayer} same scores? {scores}")

        if not isMaximizingPlayer:
            #print(f"\n{player} with {scores}, chooses {max(scores)}")
            return max(scores)
        else:
           # print(f"\n{player} with {scores}, chooses {min(scores)}")
            return min(scores)
    
    def scoreMoves(self, moves, player,opponent):
        """
        Returns an {move:score} dictionary that gives the best possible score 
        for making each move on board

        Parameter moves : A list of  (int,int) tuples
        """
        scores = {}
        for move in moves:
            scores[move] = self.evaluateMove(move,player,opponent,True,0)
        return scores
    
    def getHighestScores(self,scores_dict):
        max_score = max(scores_dict .values())
        return [key for key,score in scores_dict.items() if score == max_score ]
    
    def getRandom(self,moves):
        return moves[random.randint(0,len(moves)-1)]

    def getBestMove(self,player,opponent,moves = None):
        """
        Returns the best move for this player in the board, or NONE if there
        are no possible moves
        """
        if moves is None:
            moves = self.possibleMoves()
        if len(moves) == 0:
            return None 

        scores_dict = self.scoreMoves(moves,player,opponent)
        #print(scores_dict)
        best_moves = self.getHighestScores(scores_dict)
        #print(best_moves)
        if (1,1) in best_moves:
            res = (1,1)
        else:
            res =  self.getRandom(best_moves) #best_moves[0] #TODO: Why does introducing randommness affect optimality?
        return res


####For testing
def convertMoves(moves):
    """
    Moves is a list of string of ints
    """
    proper_moves = []
    for move in moves:
        move = int(move)
        row = move // 3    # Each row contains sorted ints in the range  1..n
        if move % 3 == 0 :
            row -= 1  
        col = (move + (3 -1)) % 3 
        proper_moves.append((row,col))
    return proper_moves



def getTestingMove(board,player,oppo,moves=None):
    board = Board(board)
    move = board.getBestMove(player,oppo,convertMoves(moves))
    r,c = move[0],move[1]
    return str(r*3 + c+1)





def test():
    player1 = X
    player2 = O
    games = 500
    games_played = games
    wins = 0
    draws = 0
    while games_played > 0:
        print(f"Progress: {((games - games_played )/ games) * 100} percent complete")
        b= [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
        ]
        board = Board(b)
        p1_won = False
        p2_won = False
        draw = False
        while not p1_won and not p2_won and not draw:
            #player1 plays
            p1_move = board.getBestMove(player1,player2)
            board.placePiece(p1_move,player1)
            board.moves_made.append(p1_move)
            #player 2
            draw = board.gameDraw()
            if not draw:
                p2_move = board.getBestMove(player2,player1)
                board.placePiece(p2_move,player2)
                board.moves_made.append(p2_move)

            else:
                draws += 1\
                
            p1_won = board.checkWin(player1)
            p2_won = board.checkWin(player2)
            if  p1_won or p2_won :
                # print(f"Player 1 {player1} won ? {p1_won} ")
                # print(f"Player 2 {player2} won ? {p2_won} ")
                #print("moves",board.moves_made)
                #print("board",board.board)
                #print("moves made ",board.moves_made)
                wins += 1

        games_played -= 1

    print(f"{wins} wins out of {games} games, so win rate is : {wins/games * 100} percent so there are {draws} draws")




#test()
# board = [
#         ["X","X","3"],
#         ["O","5","6"],
#         ["X","O","O"]
# ]
# print(getTestingMove(board,O,X))
    
# board = [[X,X,3], #0
#          [4,5,O], #1
#          [7,8,9]] #2
# #score = evaluateMove(board,(2,1),X,O,True)
# move = getBestMove(board,O,X)
# print(move)