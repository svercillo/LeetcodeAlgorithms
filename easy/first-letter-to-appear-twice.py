class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()

        for c in s:
            if c in visited:
                return c

            visited.add(c)
