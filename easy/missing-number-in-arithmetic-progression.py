class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        k = min(abs(arr[2] - arr[1]), abs(arr[1] - arr[0]))
        if arr[1] < arr[0]:
            k = -k 
        
        n = len(arr)
        for i in range(n-1):
            if arr[i+1] - arr[i] != k:
                return arr[i] + k
            
        return arr[0]
        
