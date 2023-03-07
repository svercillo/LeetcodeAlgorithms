class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        freinds_2_inds = collections.defaultdict(lambda : {})
        inds_2_freinds = collections.defaultdict(lambda : {})

        for node in range(len(preferences)): 
            for i, e in enumerate(preferences[node]):
                freinds_2_inds[node][e] = i
                inds_2_freinds[node][i] = e
        
        pair_map = {}
        for x, y in pairs:
            pair_map[x] = y
            pair_map[y] = x

        count = 0 
        for x, y in pairs:

            def is_unhappy(x, y):
                c = 0
                y_ind = freinds_2_inds[x][y]
                for ind in range(0, y_ind):
                    other_freind = inds_2_freinds[x][ind] # check if other freind prefers x over its pair

                    other_partner = pair_map[other_freind] # the partner the prefered freind is paired w

                    current_preference_score = freinds_2_inds[other_freind][other_partner]
                    x_preference_score = freinds_2_inds[other_freind][x]

                    if x_preference_score < current_preference_score: 
                        return True
                return False

            if is_unhappy(x,y): count += 1
            if is_unhappy(y, x): count += 1
                        
        return count
