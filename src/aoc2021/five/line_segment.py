from typing import List
from aoc2021.five.coord import Coord

def inclusive_range(start: int, end: int) -> range:
    if start <= end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)

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
                    for y in inclusive_range(self.a.y, self.b.y)]
        elif self.is_horizontal():
            return \
                [Coord(x, self.a.y)\
                    for x in inclusive_range(self.a.x, self.b.x)]
        else:
            return \
                [Coord(x, y)\
                    for x, y in zip(inclusive_range(self.a.x, self.b.x),
                                    inclusive_range(self.a.y, self.b.y))]
