class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        invalid = 0
        forward = 0
        for c in s:
            if c == "(":
                forward += 1
            else:
                if forward > 0:
                    forward -= 1
                else:
                    invalid += 1


        return invalid + forward
