class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        
        for c in s: 
            if c not in m:
                m[c] =1
            else: 
                m[c] +=1

        levels = {}
        for c in m:
            if m[c] not in levels: 
                levels[m[c]] = [c]
            else: 
                levels[m[c]].append(c)
        
        print(levels)
        
        # find the highest odd level
        keys = list(levels.keys())
        keys.sort()
        
        print(keys)


        odd_not_set = True
        count = 0
        for k in reversed(keys):
            if k % 2 != 0:
                if odd_not_set:
                    print("SDFSDFFD")
                    print(k)
                    count += k
                    levels[k].pop()
                    count += (k-1) * len(levels[k])

                    odd_not_set = False
                else: 
                    count += (k-1) * len(levels[k])
            else:
                count += k * len(levels[k])
        
        
        return count
  
