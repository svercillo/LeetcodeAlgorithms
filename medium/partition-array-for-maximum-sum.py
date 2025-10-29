class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def maxSum(endInd): # endind inclusive
            nonlocal k
            if endInd == -1:
                return 0

            largest = 0
            mSum = 0
            
            counter = 0
            while counter < k and endInd - counter >=0:
                startInd = endInd - counter
                if arr[startInd] > largest:
                    largest = arr[startInd]
                
                curr_sum = largest * (endInd - startInd + 1) # inclusive
                mSum = max(mSum, maxSum(startInd -1) + curr_sum)
                counter += 1

            return mSum

        return maxSum(len(arr)-1)



