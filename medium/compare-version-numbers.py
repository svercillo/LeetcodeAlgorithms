class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        swapped = False 

        if len(arr1) > len(arr2):
            swapped = True
            t = arr1
            arr1  = arr2
            arr2 = t
        
        n = len(arr1)
        m = len(arr2)

        i = 0
        while i < n:
            a1 = int(arr1[i])
            a2 = int(arr2[i])

            if a1 != a2:
                return (-1 if swapped else 1)  *  (1 if a1 > a2 else -1)

            i +=1 
        

        if n == m:
            return 0
        
        while i < m:
            a = int(arr2[i])
            if a !=0:
                return -1 * (-1 if swapped else 1)

            i +=1 
        
        return 0
