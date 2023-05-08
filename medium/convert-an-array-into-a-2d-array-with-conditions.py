class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:


        freq = defaultdict(lambda : 0)
        for e in nums:
            freq[e] += 1

        highest_freq = max([freq[e] for e in freq])

        rows = [[] for _ in range(highest_freq)]


        freq = defaultdict(lambda : 0)
        for e in nums:
            rows[freq[e]].append(e)
            freq[e] += 1

        return rows


