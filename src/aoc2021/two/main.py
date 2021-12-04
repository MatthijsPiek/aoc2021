from aoc2021.two.location import Location
from aoc2021.two.location_part_2 import LocationPart2

with open('src/aoc2021/two/input', 'r', encoding="utf-8") as f:
    data = f.read()

    location = Location()
    location.move(data)

    location_part_two = LocationPart2()
    location_part_two.move(data)

    print(f"Answer part one: {location.horizontal * location.depth}")
    print(
        f"Answer part two: {location_part_two.horizontal * location_part_two.depth}")
