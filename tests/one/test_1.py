from aoc2021.one.increases import count_increases, sum_window


def test_example_window_1():
    input_text = \
        '''199
200
208
210
200
207
240
269
260
263
'''
    increases = count_increases(input_text)
    assert increases == 7


def test_example_window_3():
    input_text = \
        '''199
200
208
210
200
207
240
269
260
263
'''
    increases = count_increases(input_text, window=3)
    assert increases == 5


def test_sum_windows():
    input = \
        [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263
        ]
    sum = sum_window(input, 3, window=3)

    assert sum == 607
