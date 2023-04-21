class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        
        mprime = 0
        for i in range(len(nums)):
            if nums[i][i] > mprime and self.is_prime(nums[i][i]):
                mprime = nums[i][i]
            
            if nums[i][len(nums) - i - 1] > mprime and self.is_prime(nums[i][len(nums) - i - 1]):
                mprime = nums[i][len(nums) - i - 1]
            

        
        return mprime
    
    
    def is_prime(self, num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
                
        return True
