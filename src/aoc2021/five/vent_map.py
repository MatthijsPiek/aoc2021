from typing import List
from aoc2021.five.line_segment import LineSegment, Coord

class VentMap:
    def __init__(self, input_string) -> None:
        self.input_string = input_string
        self.map: List[List[int]] = [[]]
        self.build_map()

    def build_map(self) -> None:
        for line in self.input_string.splitlines():
            segment = LineSegment(line)

            if ((not segment.is_horizontal()) and (not segment.is_vertical())):
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
    