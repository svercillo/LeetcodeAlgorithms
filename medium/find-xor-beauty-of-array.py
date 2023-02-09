from collections import defaultdict
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        

        freq = defaultdict(lambda : 0)


        for node in nums:
            bstr = bin(node)[2:]

            for i, c in enumerate(bstr[::-1]):
                if c == "1": 
                    freq[i] += 1 

            

        val = 0
        for i in freq:
            if freq[i] %2 == 1:
                val += 2 ** i

        return val
