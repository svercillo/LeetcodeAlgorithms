class Solution:
    def checkValidString(self, s: str) -> bool:

        
        @cache
        def is_valid(ind, count):
            if count < 0:
                return False

            n = len(s)
            if ind == n:
                return count == 0

            
            if s[ind] == "(":
                return is_valid(ind + 1, count+ 1)
            elif s[ind] == ")": 
                return is_valid(ind + 1, count - 1)
            else: # s[ind] == "*"
                return (
                    is_valid(ind + 1, count + 1) or
                    is_valid(ind + 1, count - 1) or
                    is_valid(ind + 1, count)
                )

        return is_valid(0, 0)
