class BingoCell:
    def __init__(self, value: int) -> None:
        self.value = value
        self.marked = False

    def mark(self) -> None:
        self.marked = True

    def __bool__(self) -> bool:
        return self.marked
