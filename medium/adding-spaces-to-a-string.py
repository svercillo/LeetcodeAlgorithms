class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        helper = deque()
        for i,c in enumerate(s):
            if i in spaces:
                helper.append(" ")
            helper.append(c)


        res = ""
        for c in helper:
            res += c

        return res 
