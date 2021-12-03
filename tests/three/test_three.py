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



def test_example_part_one():
    input = \
        """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
    assert most_common_characters(input) == '10110'
    assert least_common_characters(input) == '01001'