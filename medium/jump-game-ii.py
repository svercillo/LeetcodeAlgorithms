class Solution:
    def jump(self, nums) -> int:
        
        n = len(nums)         
        if n == 1: return 0
        if n <= nums[0]+1: return 1
        

        jumps = 0
        ind = 0
        while ind < n:
            # print(ind, nums[ind])
            if ind >= n -1: return jumps
            allowed = nums[ind]


            # make greedy choice at ind 
            max_val = -1
            if ind+allowed == n-1:
                return jumps +1
            # print("ind", ind, ind +1 + allowed)
            for i in range(ind+1, ind +1 + allowed):
                # gaurenteed to be gt sub_arr_max 
                if i >= n:
                    max_ind = i
                    break
                if i + nums[i] > max_val:
                    max_val = i + nums[i] 
                    max_ind =  i

            # print(max_ind)
            ind = max_ind
            jumps += 1 



        return jumps
            
