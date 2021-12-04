from aoc2021.three.main import CountPerColumn, binary_str_to_int, calc_oxygen_generator_rating, calc_co2_scrubber_rating


EXAMPLE_INPUT = \
        """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".splitlines()

def test_example_part_one():
    count = CountPerColumn(EXAMPLE_INPUT)
    assert count.most_common_characters() == '10110'
    assert count.least_common_characters() == '01001'
    
def test_binary_conversion():
    assert binary_str_to_int('10110') == 22
    assert binary_str_to_int('01001') == 9
    
def test_example_part_two():
    assert calc_oxygen_generator_rating(EXAMPLE_INPUT) == "10111"
    assert calc_co2_scrubber_rating(EXAMPLE_INPUT) == "01010"
    
def test_co2_scrubber_with_equal_counts():
    assert calc_co2_scrubber_rating(["1", "0"]) == "0"
