class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        armor = min(max(damage), armor)
        return sum(damage) - armor  + 1
