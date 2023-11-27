import heuristics
import testConstants



def assertionMessage(expected, actual):
    return f"Expected {expected}, but got {actual}"
    

def testCheckWinningMove():
        symbol_x = testConstants.BOARD_SYMBOL_X
        symbol_o = testConstants.BOARD_SYMBOL_O
        #check row and col win 
        unselected = ["3","4","5","7","8"]
        board = [["X","X","3"], 
                ["4","5","O"],
                ["7","8","O"]
                ]
        actual =  heuristics.checkWinningMove(board,unselected,symbol_x)
        assert 3 == actual , assertionMessage(3,actual)#check row 
        actual = heuristics.checkWinningMove(board,unselected,symbol_o)
        assert 3 == actual , assertionMessage(3, actual)#check col
        #check dag win
        unselected = ["3","4","8","9"]
        board = [["X","O","3"], 
                ["4","X","O"],
                ["O","8","9"]
                ]
        actual = heuristics.checkWinningMove(board,unselected,symbol_x)
        assert 9 == actual, assertionMessage(9, actual) #check diag 
        #check no possible wins for either
        unselected = ["1","3","4","8","9"]
        board = [["1","O","3"], 
                ["4","X","O"],
                ["O","8","9"]
                ]
        actual = heuristics.checkWinningMove(board,unselected,symbol_x)
        assert None == actual, assertionMessage(None, actual) # no win in one move
        actual = heuristics.checkWinningMove(board,unselected,symbol_o)
        assert None == actual, assertionMessage(None, actual)


def testCheckMiddle():
        #odd board sizes
        unselected = ["3","4","8","9", "5"]
        actual = heuristics.checkMiddle(unselected, 3 )
        assert 5 == actual, assertionMessage(5, actual)
        unselected = ["3","4","8","9"]
        actual = heuristics.checkMiddle(unselected, 3 )
        assert None== actual, assertionMessage(None, actual)
        unselected = ["3","4","8","13"]
        actual = heuristics.checkMiddle(unselected, 5 )
        expected = 13
        assert expected == actual, assertionMessage(expected, actual)

        #even board sizes, 2
        unselected = ["3"]
        expected = 3
        actual = heuristics.checkMiddle(unselected, 2)
        assert expected == actual, assertionMessage(expected, actual)
        #size 4, top left 
        unselected = ["6", "1","3", "16"]
        expected = 6
        actual = heuristics.checkMiddle(unselected, 4)
        assert expected == actual, assertionMessage(expected, actual)
        #size 4, bottom right 
        unselected = ["11", "1","3", "8", "16"]
        expected = 11
        actual = heuristics.checkMiddle(unselected, 4)
        assert expected == actual, assertionMessage(expected, actual) 


def testCheckCorner():
        #board size 1
        unselected = ["1"]
        actual = heuristics.checkCorner(unselected, 1 )
        expected = 1
        assert expected == actual, assertionMessage(expected, actual)
        #size 2
        unselected = ["3"]
        actual = heuristics.checkCorner(unselected, 2 )
        expected = 3
        assert expected == actual, assertionMessage(expected, actual)       
        #size 3
        unselected = ["2","4","8","9"]
        actual = heuristics.checkCorner(unselected, 3 )
        expected = 9
        assert expected == actual, assertionMessage(expected, actual)   
        #no corners
        unselected = ["2","4","8"]
        actual = heuristics.checkCorner(unselected, 3 )
        expected = None
        assert expected == actual, assertionMessage(expected, actual)  


def testPickHeuristicMove():
        #pick winning move
        board = [["X","X","3"], 
                ["4","5","X"],
                ["7","8","O"]
                ]
        unselected = ["3","4","5","7","8"]
        actual,_ = heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_X )
        expected = 3
        assert expected== actual, assertionMessage(expected, actual)
        #block winning move
        board = [["X","O","X"], 
                ["4","O","O"],
                ["7","8","O"]
                ]
        unselected = ["4","7","8"]
        actual,_ = heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_X )
        expected = 4
        assert expected== actual, assertionMessage(expected, actual)
        #pick middle
        board = [["1","2","3"], 
                ["4","5","6"],
                ["7","8","O"]
                ]
        unselected = ["1","2","3","4","5","6","7","8"]
        actual,_ = heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_X )
        expected = 5
        assert expected== actual, assertionMessage(expected, actual)
        #pick corner
        board = [["X","X","O"], 
                ["X","O","X"],
                ["O","8","9"]
                ]
        unselected = ["9","8"]
        actual,_ = heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_X )
        expected = 9
        assert expected== actual, assertionMessage(expected, actual)
        #pick edge
        board = [["X","X","O"], 
                ["X","O","X"],
                ["O","8","X"]
                ]
        unselected = ["8"]
        actual,_ = heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_X )
        expected = 8
        assert expected== actual, assertionMessage(expected, actual)

        board = [["O","X","X"], 
                ["X","X","6"],
                ["O","O","9"]
                ]
        unselected = ["6","9"]
        actual,_ =  heuristics.pickHeuristicMove(board, unselected, testConstants.BOARD_SYMBOL_O)
        expected = 9
        assert expected== actual, assertionMessage(expected, actual)

      

testCheckWinningMove()
testCheckMiddle()
testCheckCorner()
testPickHeuristicMove()