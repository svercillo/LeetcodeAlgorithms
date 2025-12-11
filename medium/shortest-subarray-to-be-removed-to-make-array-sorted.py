class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        r = n-1
        while r > 0:
            if arr[r-1] > arr[r]: 
                break
            r -= 1

        slen = r

        if r == 0:
            return  0


        l = 0
        while l < n - 1:
            while r < n and arr[l] > arr[r]:
                r+= 1

            if r < n:
                slen = min(slen, r - l -1) 

            if arr[l] > arr[l+1]:
                break

            l += 1

        return  min(slen, n-1- l)



        


        
