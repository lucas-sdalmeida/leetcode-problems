# todo: optimize the code
class Solution:
    def __init__(self):
        self.memo = set()

    def can_cross(self, stones: list[int]) -> bool:
        return self.try_to_cross(stones, 0, 0)

    def try_to_cross(self, stones: list[int], initial_stone_index: int, last_jump_units: int) -> bool:
        if initial_stone_index == len(stones) - 1:
            return True

        possible_jumps = self.find_possible_next_stones(stones, initial_stone_index, last_jump_units)

        if len(possible_jumps) == 0:
            return False

        for jump in possible_jumps:
            next_jump_units = stones[jump] - stones[initial_stone_index]

            if (jump, next_jump_units) in self.memo:
                continue

            there_is_a_way = self.try_to_cross(stones, jump, next_jump_units)

            if there_is_a_way:
                return True

            self.memo.add((jump, next_jump_units))

        return False

    def find_possible_next_stones(self, stones: list[int], current_stone_index: int, last_jump_units: int) -> list[int]:
        possible_jumps = []
        current_stone = stones[current_stone_index]

        for next_stone_index, stone in enumerate(stones[current_stone_index + 1:]):
            if self.can_jump_to(current_stone, stone, last_jump_units):
                possible_jumps.append(current_stone_index + next_stone_index + 1)

        return possible_jumps

    def can_jump_to(self, current_stone_units, next_stone_units, last_jump_units):
        units_between = next_stone_units - current_stone_units

        if units_between >= 0:
            return False

        return last_jump_units - 1 <= units_between <= last_jump_units + 1
