class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
    


        @cache
        def process(used, remaining, target):
            if len(remaining) == 0:
                return True

            if used == target:
                used = 0


            for c in remaining:
                if used + c <= target:
                    nremaining = list(remaining)
                    nremaining.remove(c)

                    if process(used + c, tuple(nremaining), target):
                        return True

            return False

        return process(0, tuple(nums), target)
