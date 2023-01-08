class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq = {}
        for a in answers:
            if a not in freq: 
                freq[a] = 0
            freq[a] += 1


        res = 0
        for k in freq:
            v = freq[k]
            
            if k >= v + 1:
                res += k + 1
            else:
                res += (k+1) * math.ceil(v / (k+1) )  

        return res
