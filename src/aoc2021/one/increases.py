def count_increases(text: str) -> int:
    '''
    Counts the number of times the value of the current entry is greater than
    the value of the previous entry.
    '''
    entries = [int(line.strip()) for line in text.splitlines()]
    increases = 0
    for i in range(1, len(entries)):
        if entries[i] > entries[i-1]:
            increases += 1

    return increases
