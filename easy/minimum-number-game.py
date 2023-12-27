class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort(reverse=True)
        
        res = []
        while len(nums): 
            alice = nums.pop()
            bob = nums.pop()

            
            res.append(bob)
            res.append(alice)

        return res

