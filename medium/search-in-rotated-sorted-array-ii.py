class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for e in nums:
            if e == target: 
                return True
        
        return False