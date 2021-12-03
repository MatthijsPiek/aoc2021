from aoc2021.two.location import Location
from aoc2021.two.location_part_2 import LocationPart2


def test_location_example_part_one():
    input: str = \
        """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    location = Location()

    location.move(input)

    assert location.horizontal == 15
    assert location.depth == 10

def test_location_example_part_two():
    input: str = \
        """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    location = LocationPart2()

    location.move(input)

    assert location.horizontal == 15
    assert location.depth == 60
