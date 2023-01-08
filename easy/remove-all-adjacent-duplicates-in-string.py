class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
               
        res = ""
        for c in stack:
            res += c
        return res
