class Solution:
    def goodDaysToRobBank(self, nums: List[int], time: int) -> List[int]:

        n = len(nums)
        days_decr = [0] * n
        days_incr = [0] * n

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                days_decr[i] += days_decr[i-1] +1
                
        for i in range(n-1-1, -1,-1):
            if nums[i] <= nums[i+1]:
                days_incr[i] += days_incr[i+1] + 1 

        res = []
        for i in range(n):
            if days_decr[i] >= time and days_incr[i] >= time: 
                res.append(i)

        return res

