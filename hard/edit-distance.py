class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache
        def get_min_dist(w1_ind, w2_ind):
            m = len(word1)
            n = len(word2)

            if w1_ind == m:
                return n - w2_ind # insert the rest of characters
            
            if w2_ind == n:
                return m - w1_ind # delete the remaining

            if w1_ind == m and w2_ind == n:
                return 0
        
            m_dist = math.inf
            if w1_ind < len(word1):
                if word1[w1_ind] == word2[w2_ind]:
                    m_dist = min(
                        get_min_dist(w1_ind + 1, w2_ind +1),
                        m_dist
                    ) # no op req

                m_dist = min(
                    get_min_dist(w1_ind+1, w2_ind+1) + 1,
                    m_dist
                ) # replace character

                m_dist = min(
                    get_min_dist(w1_ind + 1, w2_ind) + 1,
                    m_dist
                ) # delete character
        
            m_dist = min(
                get_min_dist(w1_ind, w2_ind+1) + 1,
                m_dist
            ) # insert character

            return m_dist


        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        # word1 = "_" + word1
        # word2 = "_" + word2

        res = get_min_dist(0, 0)
        return res if res != math.inf else -1


