class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        if n == 0:
            return 0 

    
        if n == 1 or len(set(arr)) == 1: 
            return 1


        dp = []
        for i in range(1, n-1):

            if (
                arr[i-1] > arr[i] < arr[i+1] or 
                arr[i-1] < arr[i] > arr[i+1]
            ):
                dp.append(1)
            else:
                dp.append(0)


        longest = 0
        n = len(dp)
        i = 0
        while i < n:
            j = i
            while j < n and dp[j] == 1:
                j += 1
            
            longest = max(longest, j - i)
            i = j + 1

        return longest + 2

        


