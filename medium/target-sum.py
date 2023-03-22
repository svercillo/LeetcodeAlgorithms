class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        presum = [0] * n
        npresum = [0] *n

        prefix, nprefix = 0, 0
        for i in range(n):
            prefix += nums[i]
            nprefix -= nums[i]

            presum[i] = prefix
            npresum[i] = nprefix

        @cache
        def num_ways(ind, target):

            if ind == 0:
                print(target, ind)
                if target == nums[0] or target == -nums[0]:
                    if target == nums[0] and target == -nums[0]:
                        return 2 
                    else:
                        return 1
                else:
                    return 0

                
            ways = 0
            ways += num_ways(ind-1, target - nums[ind]) # if add nums[ind] 
            ways += num_ways(ind-1, target + nums[ind]) # if subtract nums[ind]
            
            return ways
            
            



        return num_ways(len(nums)-1, target)    
