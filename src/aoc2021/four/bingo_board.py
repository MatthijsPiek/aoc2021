from typing import List, Dict
from aoc2021.four.bingo_cell import BingoCell


class BingoBoard:
    def __init__(self, board_as_text: str) -> None:
        lines = board_as_text.splitlines()
        self.rows: List[List[BingoCell]] = [[] for _ in lines]
        self.cols: List[List[BingoCell]] = [[] for _ in lines[0].split()]
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

    def sum_unmarked_cells(self) -> int:
        return sum(cell.value for cell in self.cells.values() if not cell.marked)
