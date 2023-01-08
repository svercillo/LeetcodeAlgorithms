class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        smallest = math.inf
        largest = 0
        lind = -1
        sind = -1
        n = len(nums)
        for i, n in enumerate(nums): 
            if n >= largest:
                largest = n
                lind = i
            if n < smallest:
                smallest = n
                sind = i
                
        print(sind, smallest, lind,largest)
        
        if sind > lind: 
            print(sind, lind, n)
            return sind + (len(nums) - lind -1) - 1
        
        
        print(len(nums), lind, sind)
        return sind + (len(nums) - lind -1) 
