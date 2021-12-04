from typing import List, Dict


class BingoCell:
    def __init__(self, value: int):
        self.value = value
        self.marked = False

    def mark(self):
        self.marked = True

    def __bool__(self):
        return self.marked


class BingoBoard:
    def __init__(self, board_as_text: str) -> None:
        lines = board_as_text.splitlines()
        self.rows: List[List[BingoCell]] = [[]] * len(lines)
        self.cols: List[List[BingoCell]] = [[]] * len(lines[0].split())
        self.cells: Dict[int, BingoCell] = {}
        for (row_index, line) in enumerate(lines):
            for (col_index, cell_str) in enumerate(line.split()):
                cell = BingoCell(int(cell_str))
                self.rows[row_index].append(cell)
                self.cols[col_index].append(cell)
                self.cells[int(cell_str)] = cell

    def mark(self, value: int) -> None:
        cell = self.cells.get(value)
        if cell is not None:
            cell.mark()

    def has_won(self) -> bool:
        return any(map(all, self.rows)) or any(map(all, self.cols))


class BingoGame:
    def __init__(self, text: str) -> None:
        lines = text.splitlines()
        self.calls = text.splitlines()[0].split(",")
        self.boards: List[BingoBoard] = []
        self.winners: List[BingoBoard] = []
        board_lines = []
        for line_index in range(2, len(lines)):
            if lines[line_index].strip() != "":
                board_lines.append(lines[line_index])
            else:
                if len(board_lines) > 0:
                    self.boards.append(BingoBoard("\n".join(board_lines)))
                    board_lines = []

    def play_until_win(self) -> None:
        for call in self.calls:
            for board in self.boards:
                board.mark(int(call))
                if board.has_won():
                    self.winners.append(board)
                    return


EXAMPLE_INPUT = \
    """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7


"""


def test_one_cell_bingo_board_lost():
    board = BingoBoard("1")

    board.mark(2)
    assert not board.has_won()


def test_one_cell_bingo_board_won():
    board = BingoBoard("1")

    board.mark(1)
    assert board.has_won()


def test_split_example_input():
    bingo = BingoGame(EXAMPLE_INPUT)

    assert len(bingo.boards) == 3
    assert len(bingo.calls) == 27
