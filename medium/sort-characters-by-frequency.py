from collections import OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}        
        for i in range(len(s)):
            if s[i] in m: 
                m[s[i]] += 1
            else: m[s[i]] =1
        
        od = {}
        for e in m: 
            if m[e] not in od:
                od[m[e]] = [e]
            else:
                od[m[e]].append(e)
        
        od_list = sorted([e for e in od])
        s = "" 
        for i in od_list:
            for arr_ind in range(len(od[i])):
                j = i
                while j:
                    s+= od[i][arr_ind]
                    j-=1


        return s[::-1]
