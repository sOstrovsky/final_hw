cross = 'X'
zero = 'O'
win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


class Cell:
    def __init__(self, n):
        self.n = n
        self.sign = None

    def __str__(self):
        return str(self.sign)


class Board:
    counter = 0
    game_over = False

    def __init__(self, cells: list[Cell]):
        self.grid = cells

    def draw_board(self):
        for i in range(3):
            line1 = f'{self.grid[0 + i * 3].sign if self.grid[0 + i * 3].sign is not None else " "} |'
            line2 = f'{self.grid[1 + i * 3].sign if self.grid[1 + i * 3].sign is not None else " "} |'
            line3 = f'{self.grid[2 + i * 3].sign if self.grid[2 + i * 3].sign is not None else " "}'
            print(line1, line2, line3)
            if i < 2:
                print('-' * 9)
        return ''

    def check_win(self):
        for i in win_coords:
            if self.grid[i[0]].sign == self.grid[i[1]].sign == self.grid[i[2]].sign:
                return f'Игра окончена.\nИгрок со знаком \'{self.grid[i[0]].sign}\' победил!'
        return False

    def __str__(self):
        return str(self.draw_board())

    def make_turn(self, idx: int, sign: str):
        if self.game_over:
            print('Игра окончена. Дальнейшие ходы невозможны')
            return

        if idx not in range(1, 10):
            print(f'Значение {idx} невалидно, сделайте новый ход')
        else:
            if self.grid[idx - 1].sign not in [cross, zero]:
                self.grid[idx - 1].sign = sign
                self.counter += 1

                # победа до 5 ходов невозможна, так что нет смысла проверять
                if self.counter > 4:
                    winner = self.check_win()
                    if type(winner) == str:
                        self.game_over = True
                        print(winner)
                    elif self.counter == 9:
                        self.game_over = True
                        print('Ничья')

            else:
                print('Поле занято, сделайте новый ход')


def print_result():
    cells = [Cell(i + 1) for i in range(9)]
    print(cells)
    board = Board(cells)

    print(board)

    board.make_turn(5, cross)
    print(board)
    board.make_turn(1, zero)
    print(board)
    board.make_turn(1, cross)
    print(board)
    board.make_turn(3, cross)
    print(board)
    board.make_turn(7, zero)
    print(board)
    board.make_turn(19, cross)
    print(board)
    board.make_turn(9, cross)
    print(board)
    board.make_turn(6, zero)
    print(board)
    board.make_turn(4, cross)
    print(board)
    board.make_turn(2, zero)
    print(board)
    board.make_turn(8, cross)
    print(board)
