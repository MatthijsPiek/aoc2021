from aoc2021.six.school import SchoolOfLanternFish

EXAMPLE_INPUT = "3,4,3,1,2"


def test_single_iteration():
    school = SchoolOfLanternFish(EXAMPLE_INPUT)

    school.run_iterations(1)

    assert school.size() == len([2, 3, 2, 0, 1])


def test_two_iterations():
    school = SchoolOfLanternFish(EXAMPLE_INPUT)

    school.run_iterations(2)

    assert school.size() == len([1, 2, 1, 6, 0, 8])


def test_18_iterations():
    school = SchoolOfLanternFish(EXAMPLE_INPUT)

    school.run_iterations(18)

    assert school.size() == len(
        [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8])


def test_80_iterations():
    school = SchoolOfLanternFish(EXAMPLE_INPUT)

    school.run_iterations(80)

    assert school.size() == 5934


def test_256_iterations():
    school = SchoolOfLanternFish(EXAMPLE_INPUT)

    school.run_iterations(256)

    assert school.size() == 26_984_457_539
