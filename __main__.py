from game import Game
import sys

if __name__ == '__main__':
    size = 3
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        try:
            size = int(arg)
        except ValueError:
            print(f"Invalid input {arg}. Please provide a valid input for board size.\Defaulting to 3 by 3.")
    else:
        print("No board size argument provided. Defaulting to 3 by 3.")

    game = Game(size)
    game.startGame()
