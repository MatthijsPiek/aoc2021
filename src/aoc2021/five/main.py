from aoc2021.five.vent_map import VentMap

with open('src/aoc2021/five/input', 'r', encoding='utf-8') as f:
    data = f.read()

vent_map = VentMap(data, allow_diagonal=False)
print(f"Answer part one: {vent_map.find_points_gte(2)}")
vent_map = VentMap(data, allow_diagonal=True)
print(f"Answer part two: {vent_map.find_points_gte(2)}")