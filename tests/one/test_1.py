from aoc2021.one.increases import count_increases

def test_example():
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