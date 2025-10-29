class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
        freq2 =[0 for _ in range(26)]

        for c in word2:
            i = ord(c) - 97
            freq2[i] += 1
        
        def canMakePrefix():
            for i in range(26):
                if freq[i] < freq2[i]: 
                    return False
            return True

        freq = [0 for _ in range(26)]
        l, r = 0, 0 # inclusive
        n = len(word1)

        res = 0

        while r < n:
            freq[ord(word1[r]) - 97] += 1

            if canMakePrefix():
                res += l + 1

                while l < r:
                    # incr l until you can no longer make prefix
                    
                    freq[ord(word1[l]) - 97] -= 1
                    if not canMakePrefix():
                        freq[ord(word1[l]) - 97] += 1 # put letter back
                        break

                    res += 1
                    l += 1
            r += 1 


        return res




            
