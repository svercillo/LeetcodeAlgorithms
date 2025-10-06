import heapq
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):

        n, m = len(nums1), len(nums2)
        
        value = nums1[0] + nums2[0] 
        heap = [(value, (0,0))]


        seen = set()
        res = []
        while len(heap) and k: 
            value, coord = heapq.heappop(heap)


            print(value, coord)
            l,r = coord


            if (l,r ) in seen:
                continue 

            seen.add((l,r))

            if l < n-1: 
                value = nums1[l+ 1] + nums2[r] 
                heapq.heappush(heap, (value, (l+1, r)))

            if r < m -1:
                value = nums1[l] + nums2[r+1] 
                heapq.heappush(heap, (value, (l, r+1)))

            pair = [nums1[l], nums2[r]]
            res.append(pair)
            
            k -= 1

        return res

res = Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 10)

print(res)
