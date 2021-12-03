class Location:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0
        
    def move_direction(self, direction: str, amount: int) -> None:
        if direction == 'down':
            self.depth += amount
        elif direction == 'up':
            self.depth -= amount
        elif direction == 'forward':
            self.horizontal += amount
        else:
            raise ValueError('Invalid direction')
        
    def move(self, instruction_text: str) -> None:
        for line in instruction_text.splitlines():
            direction, amount = line.split()
            self.move_direction(direction, int(amount))
        