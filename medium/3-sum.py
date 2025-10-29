class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        freq = {}
        for e in nums:
            if e not in freq:
                freq[e] = 0
            freq[e] += 1
    
        nums = sorted(list(set(nums)))
        n = len(nums)

        print( nums)
        res = set()
        for i in range(n-1): 
            for j in range(i, n):
                if nums[i]>=0:
                    continue 
                
                if i == j and freq[nums[i]] < 2:
                    continue


                req = -1 * (nums[i] + nums[j])

                if req < 0: 
                    continue

                # print(req)
                if req in freq:

                    if nums[j] != req or freq[req] > 1:

                        print(nums[i], nums[j], req)
                        res.add(tuple(sorted([nums[i], nums[j], req])))

        if 0 in freq and freq[0] >= 3:
            res.add(tuple([0,0,0]))
        return [list(e) for e in res]
                            
                    

            
