from aoc2021.five.vent_map import VentMap


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

def test_three_overlap():
    vent_map = VentMap( \
        """0,0 -> 1,0
        1,0 -> 1,1
        1,0 -> 2,0"""
    )

    assert vent_map.find_points_gte(2) == 1

def test_three_overlap_swapped():
    vent_map = VentMap( \
        """0,0 -> 0,1
        0,1 -> 1,1
        0,1 -> 0,2"""
    )

    assert vent_map.find_points_gte(2) == 1

def test_counting_empty_map():
    vent_map = VentMap("")

    assert vent_map.find_points_gte(2) == 0
    assert vent_map.find_points_gte(1) == 0
    assert vent_map.find_points_gte(0) == 0

def test_counting_single_line_single_cell():
    vent_map = VentMap("0,0 -> 0,0")

    assert vent_map.find_points_gte(1) == 1
    assert vent_map.find_points_gte(2) == 0
    assert vent_map.find_points_gte(0) == 1

def test_counting_1000_by_1000_map():
    vent_map = VentMap("0,0 -> 0,999\n0,999 -> 999,999")

    assert vent_map.find_points_gte(1) == 1999
    assert vent_map.find_points_gte(2) == 1
    assert vent_map.find_points_gte(0) == 1_000_000

def test_counting_999_by_1000_map():
    vent_map = VentMap("0,0 -> 0,999\n0,999 -> 998,999")

    assert vent_map.find_points_gte(1) == 1998
    assert vent_map.find_points_gte(2) == 1
    assert vent_map.find_points_gte(0) == 999_000
