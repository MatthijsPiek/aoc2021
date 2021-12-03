from aoc2021.three.main import most_common_characters, least_common_characters, binary_str_to_int

def test_example_part_one():
    input = \
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
"""
    assert most_common_characters(input) == '10110'
    assert least_common_characters(input) == '01001'
    
def test_binary_conversion():
    assert binary_str_to_int('10110') == 22
    assert binary_str_to_int('01001') == 9
    
    