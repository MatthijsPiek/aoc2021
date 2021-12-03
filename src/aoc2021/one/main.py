from increases import count_increases

# read input file and run the program
with open('src/aoc2021/one/input', 'r') as f:
    data = f.read()
    
    
    print(f"Increases: {count_increases(data)}")
    print(f"Increases window 3: {count_increases(data, 3)}")
    
    