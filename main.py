from board import Board
from ui import get_move

def main():
    board = Board()

    while True:
        board.display()
        move = get_move()

        success = board.apply_move(move)
        if not success:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
