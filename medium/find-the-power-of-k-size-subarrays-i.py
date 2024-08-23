class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r  = 0, k -1


        running_sum = 0
        bad_inds = set()
        for i in range(k-1):
            running_sum += nums[i]
            if nums[i] > nums[i+1]: 
                bad_inds.add(i)


        basecost = k * (k + 1) // 2 
    

        res = []
        while r < n:
            running_sum += nums[r]
            expected_sum = (nums[l] - 1) * k + basecost
            if not len(bad_inds) and expected_sum == running_sum:
                res.append(nums[r])
            else:
                res.append(-1)

            if r < n -1 and nums[r] > nums[r+1]:
                bad_inds.add(r)
                



            running_sum -= nums[l]


            bad_inds.discard(l)
            l +=1 
            r += 1



        return res
