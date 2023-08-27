class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def canConstructWithMax(_max):
            nonlocal n, index, maxSum

            if _max == 0: 
                return True

            numBefore = index
            numAfter = n - index - 1 

            def calcMinSubarrSum(highest, length):
                if length == 0:
                    return 0

                if length > highest:
                    return highest * (highest + 1) // 2  + (length - highest) * 1

                elif length < highest:
                    return highest * (highest + 1) // 2  - (highest - length) * (highest - length + 1) // 2 

                return highest * (highest + 1) // 2
            
            beforeSum = calcMinSubarrSum(_max -1, numBefore)
            afterSum = calcMinSubarrSum(_max -1, numAfter)

            # print(_max, beforeSum, afterSum)
            return (beforeSum + afterSum + _max) <= maxSum

        l, r = 0, maxSum
        while l <= r:
            m = (l + r) // 2
            if canConstructWithMax(m):
                # print('Can do ', m)
                l = m + 1
            else:
                r = m - 1

        print("SDF")
        if canConstructWithMax(l): 
            print("ABC")
            while (l + 1) < n and canConstructWithMax(l+1):
                l += 1
            return l
        else:
            print("ZXC")
            while l > 0 and not canConstructWithMax(l):
                l -= 1
            return l 

        
