class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        zipped = sorted(zip(scores, ages), key=lambda k : (k[1], k[0]))

        n = len(scores)
        
        @cache
        def best_score_ending_in_ind(ind):
            nonlocal n

            max_score = zipped[ind][0]
            i = ind + 1
            
            while i < n:

                if zipped[ind][1] == zipped[i][1] or zipped[ind][0] <= zipped[i][0]:
                    score = best_score_ending_in_ind(i) + zipped[ind][0]

                    max_score = max(
                        score, 
                        max_score
                    )
                        

                i += 1

            return max_score

        m_score = 0
        for i in range(n):
            m_score = max(
                best_score_ending_in_ind(i),
                m_score
            )
        return m_score

