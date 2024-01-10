class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        xor_total = 0
        
        for e in nums:
            xor_total ^= e
            
        diff = xor_total | k
        same = xor_total & k
        
        # print(bin(diff), bin(same))
        return abs(self.getNumOnes(same) - self.getNumOnes(diff))
                

    def getNumOnes(self, value):
        num_ones = 0
        while value:
            if value % 2 == 1:
                num_ones += 1
            value //= 2
            
        return num_ones
