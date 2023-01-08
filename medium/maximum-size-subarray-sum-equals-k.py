class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)

        longest_length = 0
        presum = 0
        postsum = 0   
        prevals = []
        postvals = {}     
        for i in range(n):
            presum += nums[i]
            postsum += nums[n-1-i]

            if presum == k:
                print(longest_length, i + 1)
                longest_length = max(longest_length, i + 1)

            if postsum == k:
                longest_length = max(longest_length, i + 1)
            
            prevals.append(presum)

            if postsum not in postvals:
                postvals[postsum] = n - 1 - i



        print(longest_length)
        totalsum = prevals[-1]
        
        for i in range(n):
            post_sum = totalsum - prevals[i] - k
            
            if post_sum in postvals:
                postsum_ind = postvals[post_sum]

                if postsum_ind > i: 
                    if postsum_ind - i + 1 > longest_length:
                        print(longest_length)
                        longest_length = max(longest_length, postsum_ind - i + -1)
        return longest_length







Maximum Size Subarray Sum Equals k - LeetCode
print(postvals), 3
