from typing import List, Dict

def count_characters_per_column(input: str) -> List[Dict]:
    # Split the input string into a list of lines
    lines = input.splitlines()
    # Get the number of columns
    columns = len(lines[0].strip())
    # Initialize a list to hold the results
    results = [{} for i in range(columns)]
    # Iterate over the lines
    for line in lines:
        # Split the line into characters
        characters = line.strip()
        # Iterate over the characters
        for i in range(len(characters)):
            # Get the character
            character = characters[i]
            # Get the column number
            column = i
            # If the character is not in the results list, add it
            if character not in results[column]:
                results[column][character] = 1
            # Otherwise, increment the count
            else:
                results[column][character] += 1
    # Return the results
    return results

def most_common_character(column: Dict[str, int]) -> str:
    # Get the character with the highest count
    character, count = max(column.items(), key=lambda x: x[1])
    # Return the character
    return character


def least_common_character(column: Dict[str, int]) -> str:
    # Get the character with the lowest count
    character, count = min(column.items(), key=lambda x: x[1])
    # Return the character
    return character


def most_common_characters(input: str):
    char_count_per_column = count_characters_per_column(input)
    
    output = ""
    for column in char_count_per_column:
        output += most_common_character(column)
        
    return output

def least_common_characters(input: str):
    char_count_per_column = count_characters_per_column(input)
    
    output = ""
    for column in char_count_per_column:
        output += least_common_character(column)
        
    return output

def binary_str_to_int(input: str) -> int:
    return int(input, 2)

if __name__ == "__main__":
    with open('src/aoc2021/three/input', 'r') as f:
        data = f.read()
        
        gamma_rate = binary_str_to_int(most_common_characters(data))
        epsilon_rate = binary_str_to_int(least_common_characters(data))
        
        print(f"Answer: {gamma_rate * epsilon_rate}")