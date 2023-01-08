class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        unique = set(["0", "1", "8"])
        flipped = set(["6", "9"])

        comp = ""
        for c in num:
            if c not in unique and c not in flipped:
                return False

            if c == "6":
                c = "9"

            elif c == "9":
                c = "6"

            comp += c

        print(comp, num)
        return comp[::-1] == num
