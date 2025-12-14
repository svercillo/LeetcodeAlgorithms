class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:        
        total = 0
        hasvalid = False
        count = 0
        countaftervalid = 0
        for e in nums:
            if e < left:
                count += 1
                countaftervalid += 1 

                total += count - countaftervalid
            elif left <= e <= right:
                hasvalid = True
                count += 1
                countaftervalid = 0

                total += count
            else:
                count = 0
                hasvalid = False
                countaftervalid = 0
        return total
