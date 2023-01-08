class Solution:
    def partitionString(self, s: str) -> int:
        unique_chars = set()

        if not s:
            return 0

        count = 1
        for c in s:
            if c in unique_chars:
                unique_chars.clear()
                count += 1

            unique_chars.add(c)

        return count
