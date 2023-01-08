class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = {}
        for i in range(len(s)):
            c = s[i]
            
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
        
        
        used = {}
        i =0

        res = []
        while i < len(s):
            c = s[i]
            
            if len(used) == 0 and i !=0:
                res.append(i)
                
            if c not in used:
                used[c] = 1
            else:
                used[c] += 1
            
            if used[c] == chars[c]:
                used.pop(c)
            
            i += 1
            
        
        if len(res):
            result = [res[0]]
            for i in range(0, len(res)-1):
                result.append(res[i+1] - res[i])
            result.append(len(s) - res[len(res) -1])

            return result
        return [len(s)]
