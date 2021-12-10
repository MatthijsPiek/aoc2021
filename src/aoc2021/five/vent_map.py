from typing import List
from aoc2021.five.line_segment import LineSegment, Coord


class VentMap:
    def __init__(self, input_string, allow_diagonal=False) -> None:
        self.input_string = input_string
        self.map: List[List[int]] = [[]]
        self.allow_diagonal = allow_diagonal

        self.build_map()

    def build_map(self) -> None:
        for line in self.input_string.splitlines():
            segment = LineSegment(line)

            if ((not self.allow_diagonal)
                and (not segment.is_horizontal())
                    and (not segment.is_vertical())):
                continue

            for coord in segment.covered_points():
                self.cover_point(coord)

    def grow_map_horizontal(self, cols: int) -> None:
        self.map.extend(
            [[0 for _ in self.map[0]]
                for _ in range(cols)]
        )

    def grow_map_vertical(self, rows: int) -> None:
        for row in self.map:
            row.extend(
                [0 for _ in range(rows)]
            )

    def cover_point(self, coord: Coord) -> None:
        if coord.x >= len(self.map):
            self.grow_map_horizontal(coord.x - len(self.map) + 1)

        if coord.y >= len(self.map[0]):
            self.grow_map_vertical(coord.y - len(self.map[0]) + 1)

        self.map[coord.x][coord.y] += 1

    def find_points_gte(self, threshold: int) -> int:
        return sum(sum(1 for point in col if point >= threshold) for col in self.map)
