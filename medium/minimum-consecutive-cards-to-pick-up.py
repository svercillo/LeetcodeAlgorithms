class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        last_inds = defaultdict(lambda : -math.inf)

        min_dist = math.inf
        for i, c in enumerate(cards):
            min_dist = min(min_dist, i - last_inds[c])
            last_inds[c] = i

        # print([(k,last_inds[k]) for k in  last_inds])
        return min_dist + 1 if min_dist != math.inf else -1
