from typing import List
from aoc2021.three.count_per_column import CountPerColumn


def binary_str_to_int(string: str) -> int:
    return int(string, 2)


def number_of_columns(line: str) -> int:
    return len(line.strip())


def filter_on_prefix(lines: List[str], prefix: str) -> List[str]:
    return [line for line in lines if line.startswith(prefix)]


def calc_oxygen_generator_rating(lines: List[str]) -> str:
    output: str = ""
    remaining_lines: List[str] = lines
    for column_index in range(number_of_columns(lines[0])):
        count = CountPerColumn(remaining_lines)
        # Take most common characters for processed columns
        output = count.most_common_characters()[:column_index+1]
        remaining_lines = filter_on_prefix(remaining_lines, output)

    return output


def calc_co2_scrubber_rating(lines: List[str]) -> str:
    output: str = ""
    remaining_lines: List[str] = lines
    for column_index in range(number_of_columns(lines[0])):
        count = CountPerColumn(remaining_lines)
        # Take most common characters for processed columns
        output = count.least_common_characters()[:column_index+1]
        remaining_lines = filter_on_prefix(remaining_lines, output)

    return output


def part_one(text: str):
    count = CountPerColumn(text.splitlines())

    gamma_rate = binary_str_to_int(count.most_common_characters())
    epsilon_rate = binary_str_to_int(count.least_common_characters())

    print(f"Answer part one: {gamma_rate * epsilon_rate}")


def part_two(text: str):
    lines = text.splitlines()

    oxygen_generator_rating = binary_str_to_int(calc_oxygen_generator_rating(lines))
    co2_scrubber_rating = binary_str_to_int(calc_co2_scrubber_rating(lines))

    print(f"Answer part two: {oxygen_generator_rating * co2_scrubber_rating}")


if __name__ == "__main__":
    with open('src/aoc2021/three/input', 'r', encoding="utf-8") as f:
        data = f.read()

    part_one(data)
    part_two(data)
