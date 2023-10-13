"""
Picks a move from the unselected list by following this set of provided heuristics
    1. If there is a winning move, take it. 
    2. If your opponent is about to win, block them. 
    3. Take middle position if possible.
    4. Take corner positions over edge positions.
"""