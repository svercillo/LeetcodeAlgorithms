class Solution:
    class Number:
        def __init__(self, val): 
            self.val = val

        def __lt__(self, other):
            return int(self.val + other.val, 2) > int(other.val + self.val, 2)
  
    def maxGoodNumber(self, nums: List[int]) -> int:
        numbers = []
        for e in nums:
            numbers.append(self.Number(bin(e)[2:]))

        numbers.sort() 
        
        return int("".join([e.val for e in numbers]), 2)
