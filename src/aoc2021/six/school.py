NEW_BORN_TIMER = 8


class SchoolOfLanternFish:
    def __init__(self, input_str):
        self.initial_fish = self.parse_input(input_str)
        self.fish_by_timer = [0 for _ in range(NEW_BORN_TIMER + 1)]
        for fish in self.initial_fish:
            self.fish_by_timer[fish] += 1

    def parse_input(self, input_str):
        return [int(x) for x in input_str.split(",")]

    def run_iterations(self, iterations):
        for _ in range(iterations):
            self.run_one_iteration()

    def run_one_iteration(self):
        new_fish_by_timer = [0 for _ in range(NEW_BORN_TIMER + 1)]
        for i in range(1, NEW_BORN_TIMER + 1):
            new_fish_by_timer[(i - 1)] = self.fish_by_timer[i]

        new_fish_by_timer[8] = self.fish_by_timer[0]
        new_fish_by_timer[6] += self.fish_by_timer[0]

        self.fish_by_timer = new_fish_by_timer

    def size(self):
        return sum(self.fish_by_timer)

    def __repr__(self):
        return f"{self.initial_fish}"
