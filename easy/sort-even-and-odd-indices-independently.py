class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        for i,n in enumerate(nums):
            if i % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
    
        even.sort()
        odd.sort(reverse=True)
        i = 0 
        while i < len(nums):
            nums[i] = even[i // 2]
            if i //2 < len(odd):
                nums[i+1] = odd[i //2]
            i += 2
        return nums
