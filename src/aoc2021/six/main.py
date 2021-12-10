from aoc2021.six.school import SchoolOfLanternFish

with open('src/aoc2021/six/input', 'r', encoding='utf-8') as f:
    data = f.read()

school = SchoolOfLanternFish(data)
school.run_iterations(80)

print(f"Answer part one: {school.size()}")
school.run_iterations(256-80)
print(f"Answer part two: {school.size()}")
