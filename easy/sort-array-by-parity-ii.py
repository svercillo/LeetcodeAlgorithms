class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = deque()
        even = deque()
        
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        
        print(even, odd)
        
        i = 0
        while i < len(nums):
            print("here")
            nums[i] = even.popleft()
            nums[i+1] = odd.popleft()
            
            i += 2
            
        return nums
