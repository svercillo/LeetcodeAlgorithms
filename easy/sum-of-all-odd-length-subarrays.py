class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        total_sum = 0
        for i in range(n):
            start, end = i, i
            subarr_sum = 0
            while start >= 0 and end < n:   
                subarr_sum += arr[start] + arr[end]
                if start == end:
                    subarr_sum -= arr[end]


                total_sum += subarr_sum
                start -= 1
                end += 1


        return total_sum

        print(dp)
