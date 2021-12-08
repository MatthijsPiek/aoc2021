class Coord:
    @classmethod
    def from_str(cls, coord_str: str):
        return cls(*map(int, coord_str.split(',')))

    def __init__(self, coord_x: int, coord_y: int) -> None:
        self.x = coord_x  # pylint: disable=invalid-name
        self.y = coord_y  # pylint: disable=invalid-name
