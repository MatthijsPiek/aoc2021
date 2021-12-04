from aoc2021.four.bingo_game import BingoGame

with open('src/aoc2021/four/input', 'r', encoding='utf-8') as f:
    data = f.read()

bingo: BingoGame = BingoGame(data)
bingo.play_until_win()

if bingo.last_call is not None:
    print(f"Answer: {bingo.last_call * bingo.winners[0].sum_unmarked_cells()}")

bingo.play_until_last_win()
if bingo.last_call is not None:
    print(
        f"Answer part two: {bingo.last_call * bingo.winners[-1].sum_unmarked_cells()}")
