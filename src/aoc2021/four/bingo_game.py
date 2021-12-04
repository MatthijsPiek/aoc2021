from typing import List, Optional
from aoc2021.four.bingo_board import BingoBoard


class BingoGame:
    def __init__(self, text: str) -> None:
        lines = text.splitlines()
        self.calls = lines[0].split(",")
        self.boards: List[BingoBoard] = []
        self.winners: List[BingoBoard] = []
        self.last_call: Optional[int] = None
        board_lines = []
        for line_index in range(2, len(lines)):
            if lines[line_index].strip() != "":
                board_lines.append(lines[line_index])
            else:
                if len(board_lines) > 0:
                    self.boards.append(BingoBoard("\n".join(board_lines)))
                    board_lines = []

    def play_until_win(self, min_winners=1) -> None:
        for call in self.calls:
            self.last_call = int(call)
            for board in self.boards:
                board.mark(int(call))
                if board.has_won():
                    if board not in self.winners:
                        self.winners.append(board)
                    if len(self.winners) >= min_winners:
                        return

    def play_until_last_win(self) -> None:
        self.play_until_win(min_winners=len(self.boards))
