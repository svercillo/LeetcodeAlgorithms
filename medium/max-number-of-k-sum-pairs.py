class Solution:
    def maxOperations(self, nums, k: int) -> int:
        freq = {}
        for e in nums:
            if e not in freq:
                freq[e] = 0

            freq[e] += 1

        
        print(freq)
        count = 0
        for e in freq:
            print(e, k / 2, k -e )
            if e < k / 2 and k -e in freq:
                print(e, k / 2, k -e )
                count += min(freq[e], freq[k -e])
            elif e == k / 2:
                count += freq[e] // 2
            

        return count 
    
