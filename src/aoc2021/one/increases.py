def sum_window(entries: list, i: int, window: int) -> int:
    '''
    Returns the sum of the values in the window of size `window` starting at
    `i`.
    '''
    return sum(entries[i - window:i])

def count_increases(text: str, window: int = 1) -> int:
    '''
    Counts the number of times the value of the current entry is greater than
    the value of the previous entry, in a sliding window of size `window`.
    '''
    entries = [int(line.strip()) for line in text.splitlines()]
    increases = 0
    for i in range(window, len(entries)):
        if sum_window(entries, i, window) > sum_window(entries, i - 1, window):
            increases += 1

    return increases
