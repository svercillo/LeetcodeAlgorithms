
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        if not needle: return 0
        
        
        start = 0
        end = 0
        
        n = len(haystack)
        while start < len(haystack):
            
            if end - start  == len(needle) : 
                if haystack[start: end] == needle:
                    return start
                elif end == n:
                    return -1
                else:
                    start += 1
                    end +=1
            elif end - start < len(needle):
                end += 1 
            
        return -1
