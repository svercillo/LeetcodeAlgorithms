class Solution:

    MOD = 10 ** 9 + 7


    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        if multiplier == 1:
            return nums 
        seen = set()
        heap = []

        for i,e in enumerate(nums):
            heapq.heappush(heap, (e, i))

        for ops in range(k):
            e, i = heapq.heappop(heap)
            nums[i] *= multiplier 
        
            heapq.heappush(heap, (nums[i], i))
            seen.add(i)

            if len(seen) == len(nums):
                break
        
        # print(nums)
        remaining_k = k - (ops + 1)

        baseline = remaining_k // len(nums)
        left_to_do = remaining_k % len(nums)

        # print(baseline, left_to_do)

        if baseline:
            for i in range(len(nums)):
                nums[i] *= pow(multiplier, baseline, self.MOD)
                nums[i] %= self.MOD

        for _ in range(left_to_do):
            e, i = heapq.heappop(heap)
            nums[i] *= multiplier
            nums[i] %= self.MOD

        for i in range(len(nums)):
            nums[i] %= self.MOD

        return nums
        
