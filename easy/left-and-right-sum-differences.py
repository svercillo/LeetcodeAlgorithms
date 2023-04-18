class Solution:
    def leftRigthDifference(self, nums):
        n = len(nums)
        presum_arr = [0] * n
        postsum_arr = [0] * n

        presum = 0
        postsum = 0
        
        for i in range(len(nums)):
            presum += nums[i]
            postsum += nums[len(nums) - 1 - i]

            presum_arr[i] = presum
            postsum_arr[n-1- i] = postsum

        answer = []
        for i in range(len(nums)):
            if i == 0:
                left = 0
            else:
                left = presum_arr[i-1]
            
            if i == n -1:
                right = 0
            else:
                right = postsum_arr[i +1]

            answer.append(abs(left-right))

        
        return answer