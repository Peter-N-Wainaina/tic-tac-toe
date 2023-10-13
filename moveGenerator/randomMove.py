"""
This module picks a move at random.
"""
import random

def pickComputerMove(unselected):
    """
    Returns a random element in unselected cast to an int, and 
    removes the selected move from unselected. It also returns
    this modified unselected list. 

    unselected : A list of string of ints. 
    """
    move_index = random.randint(0,len(unselected)-1)
    move =  unselected[move_index]
    unselected.remove(move)
    return int(move), unselected