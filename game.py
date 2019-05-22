from board import Board
from enemy import Enemy
import time


class Game:
    """
    Created to run tic-tac-toe game
    """
    def __init__(self):
        self.board = Board()

    @staticmethod
    def start_with():
        while True:
            answer = input("Choose who moves first (user, bot): ")
            if answer in {'user', 'bot'}:
                return answer
            else:
                print('Must be user or bot!')

    def bot_starts(self):
        bot = Enemy(self.board, 'O')
        print(self.board)
        time.sleep(1.5)
        while not self.board.check_state():
            print('\nComputer chooses\n')
            bot.make_move()
            print(self.board)
            if not self.board.check_state():
                print('\nPlayer chooses:')
                # second.make_move()
                while True:
                    try:
                        position = (int(input("Write x: ")), int(input("Write y: ")))
                        self.board.put("X", position[1], position[0])
                        break
                    except IndexError as e:
                        print(e)
                    except ValueError:
                        print("Write only digit coords")
                print(self.board)

        if self.board.check_state() == "X":
            print('Congratulation!')
            print("You win!")
        elif self.board.check_state() == "O":
            print(":(")
            print("Computer win!")
        else:
            print(self.board.check_state())

    def player_starts(self):
        bot = Enemy(self.board, 'O')
        print(self.board)
        while not self.board.check_state():
            if not self.board.check_state():
                print('\nPlayer chooses:')
                # second.make_move()
                while True:
                    try:
                        position = (int(input("Write x: ")), int(input("Write y: ")))
                        self.board.put("X", position[1], position[0])
                        break
                    except IndexError as e:
                        print(e)
                    except ValueError:
                        print("Write only digit coords")
                print(self.board)

            print('\nComputer chooses\n')
            if self.board.is_free_cell():
                bot.make_move()
            print(self.board)

        if self.board.check_state() == "X":
            print('Congratulation!')
            print("You win!")
        elif self.board.check_state() == "O":
            print(":(")
            print("Computer win!")
        else:
            print(self.board.check_state())

    def play(self):
        if Game.start_with() == "user":
            self.player_starts()
        else:
            self.bot_starts()


if __name__ == '__main__':
    game = Game()
    game.play()
