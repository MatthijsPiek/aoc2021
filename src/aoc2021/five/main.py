from aoc2021.five.vent_map import VentMap

with open('src/aoc2021/five/input', 'r', encoding='utf-8') as f:
    data = f.read()

vent_map = VentMap(data)
print(f"Answer: {vent_map.find_points_gte(2)}")
