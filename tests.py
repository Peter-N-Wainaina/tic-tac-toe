"""
Test cases for all tictactoe classes
"""
import player
from  board import Board
from game import Game
import time
def testPlayer():
    """
    Test function to verify the (human) Player class
    """
    print("Testing the Player class")

    p1 = player.Player("x")
    assert ("X" == p1.getSymbol())   
    assert ((1,1) ==  p1.convertMove(Board(3,[]),5))
    assert ((3,3) ==  p1.convertMove(Board(4,[]),16))

def testBoard():
    """
    Test function to verify the Board class 
    """
    print("Testing the Board class")
    #test init
    b1 = Board(3,[])   
    expected_board = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]
    moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    assert b1.getBoard() == expected_board
    assert b1.getDimension() == 3
    assert b1.getMoves() == []
    assert sorted(b1.possibleMoves()) == sorted(moves)

    init_board = [
        ["X","Q","3"],
        ["4","M","6"],
        ["7","B","9"]
    ]
    init_moves = [(0,0),(0,1),(1,1),(2,1)]
    b2 = Board(3,init_moves,init_board)
    assert b2.getBoard() == init_board
    assert b2.getMoves() == init_moves

    #test clear 
    b2.clear()
    assert b2.getBoard() == expected_board
    assert b1.getDimension() == 3
    assert b1.getMoves() == []

    #test piece placement and removal
    p1 = player.Player("X")
    b2.makeMove(p1,(1,1))
    expected_board = [
        ["1","2","3"],
        ["4","X","6"],
        ["7","8","9"]
    ]
    assert expected_board == b2.getBoard()
    assert b2.getMoves() == [(1,1)]

    p2 = player.Player("O")
    b2.makeMove(p2,(2,0))
    expected_board1 = [
        ["1","2","3"],
        ["4","X","6"],
        ["O","8","9"]
    ]
    assert expected_board1 == b2.getBoard()
    assert b2.getMoves() == [(1,1),(2,0)]
    assert sorted(b2.possibleMoves()) == sorted([(0,0),(0,1),(0,2),(1,0),(1,2),\
                                                 (2,1),(2,2)])
    b2.undoMove((2,0))
    assert expected_board == b2.getBoard()
    assert b2.getMoves() == [(1,1)]
    assert sorted(b2.possibleMoves()) == sorted([(0,0),(0,1),(0,2),(2,0),(1,0),\
                                                 (1,2),(2,1),(2,2)])
    #test isBoardFull
    assert b2.isBoardFull() == False
    full_board = [
        ["A","B","X"],
        ["A","B","X"],
        ["A","B","X"],
    ]
    full_board = Board(3,[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),\
                                (2,1),(2,2)],full_board)
    assert full_board.isBoardFull()

    #test winning functions
    #horiz win
    p1 = player.Player("x")
    b = [
        ["1","2","3"],
        ["4","X","6"],
        ["X","8","X"]
    ]
    b1 = Board(3,[(1,1),(2,0),(2,2)],b)
    assert not b1.hasWon(p1,3)
    b1.makeMove(p1,(2,1))
    assert  b1.hasWon(p1,3)
    # vert win
    b1.makeMove(p1,(0,0))
    b1.makeMove(p1,(1,0))
    assert  b1.hasWon(p1,3)
    b1.undoMove((1,0))
    b1.undoMove((2,1))
    b1.undoMove((2,2))
    assert not b1.hasWon(p1,3)
    # primary diag win 
    b1.makeMove(p1,(2,2))
    assert  b1.hasWon(p1,3)
    #second diag
    b1.undoMove((0,0))
    b1.makeMove(p1,(0,2))
    assert  b1.hasWon(p1,3)

    #Test get center pieces
    b_dim3 = Board(3)
    assert b_dim3.getCenterPieces() == [(1,1)]
    b_dim2 = Board(2)
    assert sorted(b_dim2.getCenterPieces()) == sorted([(0,0),(0,1),(1,0),(1,1)])
    b_dim6 =  Board(6)
    assert sorted(b_dim6.getCenterPieces()) == sorted([(2,2),(2,3),(3,2),(3,3)])

    # Test Get Best Move for odd dim 
    scores = {(0,0):10,(1,0):7}
    ai_player = player.AIPlayer("X")
    assert ai_player._getBestMove(scores,b_dim3) == (0,0)
    scores[(1,1)] = 9
    assert ai_player._getBestMove(scores,b_dim3) == (0,0)
    scores[(1,1)] = 10
    assert ai_player._getBestMove(scores,b_dim3) == (1,1)
    #for even dim 
    scores = {(0,0):1,(1,0):7,(2,2):10,(3,3):10}
    assert ai_player._getBestMove(scores,b_dim6) in [(2,2),(3,3)]

def simulateGames():
    player1 = player.AIPlayer("X")
    player2 = player.AIPlayer("O")
    games = 10
    games_played = games
    wins = 0
    draws = 0
    while games_played > 0:
        print(f"Progress: {((games - games_played )/ games) * 100} percent complete")
        board = Board(3)
        p1_won = False
        p2_won = False
        draw = False
        while not p1_won and not p2_won and not draw:
            #player1 plays
            p1_move = player1.chooseMove(board,player2)
            board.makeMove(player1,p1_move)
            #player 2
            draw = board.isBoardFull()
            if not draw:
                p2_move = player2.chooseMove(board,player1)
                board.makeMove(player2,p2_move)
            else:
                draws += 1\
                
            p1_won = board.hasWon(player1)
            p2_won = board.hasWon(player2)
            if  p1_won or p2_won :
                wins += 1
        games_played -= 1
    print(f"{wins} wins out of {games} games, so win rate is : {wins/games * 100} percent so there are {draws} draws")
    
def testGame():
    print("Testing the Game class")
    g1 = Game(3)
    g1.startGame()
    pass

testPlayer()
testBoard()
#testGame()
# start_time = time.time()
# simulateGames()
# end_time = time.time()
# print(f"The simulation took {end_time - start_time} seconds to run ")

print("All test cases passed")