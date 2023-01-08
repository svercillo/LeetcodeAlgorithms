class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        operation = True
        while operation:
            operation = False
            tarr = arr.copy()
            for i in range(1, n-1):
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    operation = True
                    tarr[i] -= 1
                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    operation = True
                    tarr[i] += 1
                    
            arr = tarr
            
        return arr
            
