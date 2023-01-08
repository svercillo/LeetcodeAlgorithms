
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        
        n = len(nums)
        forward = []
        s = 0
        for e in nums:
            s += e
            forward.append(s)
            
        backward = []
        s = 0
        for e in nums[::-1]:
            s += e
            backward.append(s)
                    

        fmax = [0] * (firstLen - 1 )
        fmax.append(sum(nums[:firstLen]))
        fsum = fmax[-1]

        bmax = [0] * (firstLen -1)
        bmax.append(sum(nums[n - firstLen: n]))
        bsum = bmax[-1]
        print(nums[n - firstLen: n], sum(nums[n - firstLen: n]))
        print("bsum", bsum)

        for i in range(firstLen, n):            
            fsum -= nums[i - firstLen]
            fsum += nums[i]
            fmax.append(max(fmax[-1], fsum))            
            

        for i in range(n-1- firstLen, -1, -1):
            bsum -= nums[i + firstLen]
            bsum += nums[i]
            bmax.append(max(bmax[-1], bsum))
        
        bmax = bmax[::-1]

    
        ssum = sum(nums[:secondLen])
        _max = ssum + bmax[secondLen]
        
        for i in range(secondLen, n):
            ssum -= nums[i - secondLen]
            ssum += nums[i]
            # print(ssum)
            _max = max(_max, max(bmax[i + 1] if i +1 < n else 0, fmax[i - secondLen]) + ssum)
            
        return _max
