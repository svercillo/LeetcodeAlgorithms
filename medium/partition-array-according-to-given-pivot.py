class Solution:
    def pivotArray(self, nums: List[int], k: int) -> List[int]:

        lt_k = deque()
        eq_k = deque()
        gt_k = deque() 

        for i,n in enumerate(nums):
            if n < k:
                lt_k.append(n)
            elif n == k:
                eq_k.append(n)
            elif n > k:
                gt_k.append(n)


        i = 0
        for n in lt_k:
            nums[i] = n        
            i += 1

        for n in eq_k:
            nums[i] = n        
            i += 1

        for n in gt_k:
            nums[i] = n
            i += 1

        return nums
