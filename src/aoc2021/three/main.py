from typing import List, Dict


class CountPerColumn:
    def __init__(self, lines: List[str]) -> None:
        self.lines = lines
        self.columns = len(self.lines[0].strip())
        self.results = []
        self.count_characters_per_column()
    
    def count_characters_per_column(self) -> None:
        # Initialize a list to hold the results
        self.results = [{} for i in range(self.columns)]
        # Iterate over the lines
        for line in self.lines:
            characters = line.strip()
            # Iterate over the characters
            for i in range(len(characters)):
                # Get the character
                character = characters[i]
                # Get the column number
                column = i
                # If the character is not in the results list, add it
                if character not in self.results[column]:
                    self.results[column][character] = 1
                # Otherwise, increment the count
                else:
                    self.results[column][character] += 1
                    
    def most_common_character(self, column: Dict[str, int]) -> str:
        # Get the character with the highest count
        character, count = max(column.items(), key=lambda x: x[1])

        return character

    def least_common_character(self, column: Dict[str, int]) -> str:
        # Get the character with the lowest count
        character, count = min(column.items(), key=lambda x: x[1])
        
        return character


    def most_common_characters(self) -> str:        
        output = ""
        for column in self.results:
            output += self.most_common_character(column)
            
        return output

    def least_common_characters(self) -> str:
        output = ""
        for column in self.results:
            output += self.least_common_character(column)
            
        return output

def binary_str_to_int(input: str) -> int:
    return int(input, 2)

def oxygen_generator_rating(input: str) -> int:
    pass    
    
if __name__ == "__main__":
    with open('src/aoc2021/three/input', 'r') as f:
        data = f.read()
        
        count = CountPerColumn(data.splitlines())
        
        gamma_rate = binary_str_to_int(count.most_common_characters(data))
        epsilon_rate = binary_str_to_int(count.least_common_characters(data))
        
        print(f"Answer: {gamma_rate * epsilon_rate}")