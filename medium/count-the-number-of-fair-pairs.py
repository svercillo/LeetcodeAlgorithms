from bisect import bisect_left, bisect_right
class Solution:
            
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        _sorted = sorted(nums)
        num_pairs = 0
        
        for i, num in enumerate(_sorted): 
            smallest = lower - num    
            largest = upper - num 
            
            sind = bisect_left(_sorted, smallest, lo=i+1, hi=len(nums))
            lind = bisect_right(_sorted, largest, lo=sind)

            if lind <= sind:
                continue
            print(num, sind, lind)

            num_pairs += lind - sind
                
        return num_pairs
