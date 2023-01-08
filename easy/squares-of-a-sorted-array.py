class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        arr = [] 
        for n in nums: 
            arr.append(n **2)
            
        return sorted(arr)
