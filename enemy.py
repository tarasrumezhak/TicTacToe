from btree import LinkedBinaryTree
from random import randrange
from copy import deepcopy


class Enemy:
    """
    Representation of bot-instance player
    """
    SIGN = "O"

    def __init__(self, board, mark):
        self.mark = mark
        self.game_board = board

    @staticmethod
    def calculate(board):
        """
        Calculates the score to make the best decision
        board: Board
        """
        curr_tree = LinkedBinaryTree(board)

        def recurse(tree):
            """
            Recursive function to estimate all randomly chosen variants
            decision: LinkedBinaryTree
            return: int
            """
            brd = tree.get_root_val()
            condition = brd.check_state()

            if not condition:
                available = brd.find_empty()
                person_move = available.pop(randrange(len(available)))
                brd.put("X", person_move[0], person_move[1])

                if len(available) > 1:
                    m1 = available.pop(randrange(len(available)))
                    m2 = available.pop(randrange(len(available)))
                    tree.insert_left(make_move(brd, m1, Enemy.SIGN))
                    tree.insert_right(make_move(brd, m2, Enemy.SIGN))
                    return recurse(tree.get_right_child()) + recurse(tree.get_left_child())

                elif len(available) == 1:
                    m1 = available.pop(randrange(len(available)))
                    tree.insert_left(make_move(brd, m1, Enemy.SIGN))
                    return recurse(tree.get_left_child())

                else:
                    return recurse(tree)

            elif condition.startswith('D'):
                return 0
            elif condition.startswith('X'):
                return -1
            elif condition.startswith("O"):
                return 1

        def make_move(brd, pos, mark):
            """
            brd: game board with current condition
            pos: coordinates of position to add a mark
            mark: player mark in game
            return: board with added mark
            """
            brd = deepcopy(brd)
            brd.put(mark, pos[0], pos[1])
            return brd
        return recurse(curr_tree)

    def try_to_move(self, position):
        """
        Playing a scenario of move
        position: coordinates of position of the first move
        """
        brd = deepcopy(self.game_board)
        brd.put(self.mark, position[0], position[1])
        decision = Enemy.calculate(brd)
        return decision

    def turn(self):
        """
        Computer turn
        """
        available = self.game_board.find_empty()
        available2 = deepcopy(available)
        for j, i in enumerate(available2):
            new_brd = deepcopy(self.game_board)
            new_brd.put(self.mark, i[0], i[1])
            if new_brd.check_state() == "O":
                self.game_board.put(self.mark, i[0], i[1])
                available.pop(j)
                return

        available3 = deepcopy(available)
        for j, i in enumerate(available3):
            new_brd2 = deepcopy(self.game_board)
            new_brd2.put("X", i[0], i[1])
            if new_brd2.check_state() == "X":
                self.game_board.put(self.mark, i[0], i[1])
                available.pop(j)
                return

        if len(available) > 1:
            move1 = available.pop(randrange(len(available)))
            decision1 = self.try_to_move(move1)
            move2 = available.pop(randrange(len(available)))
            decision2 = self.try_to_move(move2)
            decision = max((decision1, move1), (decision2, move2))[1]
            self.game_board.put(self.mark, decision[0], decision[1])
        else:
            move = available[0]
            self.game_board.put(self.mark, move[0], move[1])

    def make_move(self):
        """
        Making a move in the game
        """
        return self.turn()


if __name__ == '__main__':
    from board import Board
    board = Board()
    enemy = Enemy(board, "O")
    board.put("X", 1, 1)
    board.put("X", 1, 3)
    enemy.make_move()
    print(board)
