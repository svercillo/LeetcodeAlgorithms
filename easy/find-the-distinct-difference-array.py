class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [0] * n
        sufix = [0] * n
        preset = set()
        sufset = set()
        
        for i in range(n):
            preele = nums[i]
            sufele = nums[n-1 -i]
            preset.add(preele)
            sufset.add(sufele)

            prefix[i] = len(preset)

            sufix[n-1 -i] = len(sufset)

        print(prefix, sufix)

        res = []
        for i in range(n):
            if i == n -1:
                res.append(prefix[i])
            else: 
                res.append(prefix[i] - sufix[i+1])

            


        return res 
            
