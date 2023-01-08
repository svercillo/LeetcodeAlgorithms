class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        k = 0
        lt_k = deque()
        gt_k = deque()

        for i,n in enumerate(nums):
            if n < k:
                lt_k.append(n)
            elif n >= k:
                gt_k.append(n)

        i = 0
        for n in gt_k:
            nums[i] = n
            nums[i+1] = lt_k.popleft()
            i += 2

        return nums
