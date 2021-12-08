from typing import List
from aoc2021.five.coord import Coord

class LineSegment:
    def __init__(self, segment_str: str) -> None:
        coord_a, coord_b = \
            map(
                Coord.from_str,
                segment_str.split(' -> '))

        self.a, self.b = coord_a, coord_b  # pylint: disable=invalid-name

    def is_vertical(self) -> bool:
        return self.a.x == self.b.x

    def is_horizontal(self) -> bool:
        return self.a.y == self.b.y

    def covered_points(self) -> List[Coord]:
        if self.is_vertical():
            return \
                [Coord(self.a.x, y)\
                    for y in range(min(self.a.y, self.b.y), max(self.a.y, self.b.y) + 1)]
        elif self.is_horizontal():
            return \
                [Coord(x, self.a.y)\
                    for x in range(min(self.a.x, self.b.x), max(self.a.x, self.b.x) + 1)]
        else:
            raise ValueError('Line segment is not vertical or horizontal')
