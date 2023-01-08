class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0
        for c in text:
            if c == " ":
                count += 1

        words = text.split()
        if count == 0:
            return text

        if len(words) == 1:
            return words[0] + " " * count

        n = len(words) - 1

        s = ""
        for i in range(len(words)):
            w = words[i]

            s += w
            if i != len(words) - 1:
                s += " " * (count // n)

        s += " " * (count % (n))
        return s
