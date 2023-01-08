class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        arr = sorted(heights)

        cnt = 0
        for i in range(len(arr)):
            if arr[i] != heights[i]: 
                cnt += 1            
        return cnt
    
