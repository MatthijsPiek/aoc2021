from increases import count_increases

# read input file and run the program
with open('src/aoc2021/one/input', 'r') as f:
    data = f.read()
    
    increases = count_increases(data)
    
    print(f"Increases: {increases}")