from typing import List


class Coord:
    @classmethod
    def from_str(cls, coord_str: str):
        return cls(*map(int, coord_str.split(',')))

    def __init__(self, coord_x: int, coord_y: int) -> None:
        self.x = coord_x  # pylint: disable=invalid-name
        self.y = coord_y  # pylint: disable=invalid-name


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


class VentMap:
    def __init__(self, input_string) -> None:
        self.input_string = input_string
        self.map: List[List[int]] = [[]]
        self.build_map()

    def build_map(self) -> None:
        for line in self.input_string.splitlines():
            segment = LineSegment(line)

            if (not segment.is_horizontal() and not segment.is_vertical()):
                continue

            for coord in segment.covered_points():
                self.cover_point(coord)

    def cover_point(self, coord: Coord) -> None:
        if coord.x >= len(self.map):
            self.map.extend([[0] * len(self.map[0])] *
                            (coord.x - len(self.map) + 1))

        if coord.y >= len(self.map[0]):
            for row in self.map:
                row.extend([0] * (coord.y - len(row) + 1))

        self.map[coord.x][coord.y] += 1

    def find_points_gte(self, threshold: int) -> int:
        return sum(sum(1 for point in col if point >= threshold) for col in self.map)


EXAMPLE_INPUT = \
    """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_example_input_part_one():
    vent_map = VentMap(EXAMPLE_INPUT)

    assert vent_map.find_points_gte(2) == 5
