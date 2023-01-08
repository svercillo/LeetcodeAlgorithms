class Solution:
    def largestInteger(self, num: int) -> int:
        
        even = []
        odd = []
        
        s = str(num)
        even_odd = [False] * len(s)
        for i,c in enumerate(s):
            dig = int(c)
            if dig % 2 ==0:
                even_odd[i] = True
                even.append(str(dig))
            else:
                odd.append(str(dig))
                
                
        even.sort()
        odd.sort()
        res = [c for c in s]
        for i in range(len(s)):
            if even_odd[i]:
                res[i] = even.pop()
            else:
                res[i] = odd.pop()
                
        
        result = ""
        for c in res:
            result += c
        return result
