import cmd
import random

BOARD_SIZE = 100
SHIFT_PROBABILITY = 0.2


def print_board(board):
    for i in range(10):
        line = ""
        for j in range(10):
            if board[i * 10 + j] == -1:
                line += " .. "
            else:
                line += " {:0>2d} ".format(board[i * 10 + j])
        print(line)


class SnakesAndLadders(cmd.Cmd):
    intro = "Welcome to snakes and ladders!"
    prompt = "> "
    file = None
    players = []
    board = []

    def do_gen(self, arg):
        self.board = []
        for i in range(BOARD_SIZE):
            if random.random() < SHIFT_PROBABILITY:
                self.board.append(random.randrange(BOARD_SIZE))
            else:
                self.board.append(-1)
        print_board(self.board)

    def do_quit(self, arg):
        return True


if __name__ == "__main__":
    SnakesAndLadders().cmdloop()
