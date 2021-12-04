from typing import List, Dict


class CountPerColumn:
    def __init__(self, lines: List[str]) -> None:
        self.lines = lines
        self.columns = len(self.lines[0].strip())
        self.results: List[Dict[str, int]] = []
        self.count_characters_per_column()

    def count_characters_per_column(self) -> None:
        # Initialize a list to hold the results
        self.results = [{} for i in range(self.columns)]
        # Iterate over the lines
        for line in self.lines:
            characters = line.strip()
            # Iterate over the characters
            for column, character in enumerate(characters):
                # If the character is not in the results list, add it
                if character not in self.results[column]:
                    self.results[column][character] = 1
                # Otherwise, increment the count
                else:
                    self.results[column][character] += 1

    def most_common_character(self, column: Dict[str, int]) -> str:
        # Get the character with the highest count if equal prefer "1"
        character, _ = max(
            column.items(), key=lambda x: (x[1], x[0] == "1"))
        return character

    def least_common_character(self, column: Dict[str, int]) -> str:
        # Get the character with the lowest count if equal prefer "0"
        character, _ = min(
            column.items(), key=lambda x: (x[1], x[0] == "1"))
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
