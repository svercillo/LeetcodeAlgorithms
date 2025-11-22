from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        compressed = []
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == "*":
                compressed.append((p[i], 1))
                i += 1
            else:
                compressed.append((p[i], 0))
            i += 1

        p = compressed
        
        @cache
        def possible(sind, pind):
            if pind == len(p): 
                return sind == len(s)


            print(s[sind:], p[pind:])


            pc, specialp = p[pind]

            if sind == len(s):
                if specialp:
                    return possible(sind, pind + 1)

                else:
                    return pind == len(p)


            isvalid = False
            if specialp:
                # don't use the character
                isvalid |= possible(sind, pind + 1)
                    
                
                if s[sind] == pc or pc == ".":
                    # use the character another itme
                    isvalid |= possible(sind + 1, pind)

            else:

                if pc == "." or s[sind] == pc:
                    isvalid |= possible(sind+ 1, pind + 1)
                
            
            return isvalid
            

        return possible(0, 0)
