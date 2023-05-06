class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        
        star_score = [v for v in vals]
        star_size = [0 for v in vals]

        dir_edges = []

        for i, j in edges:
            dir_edges.append((i, j, vals[j]))
            dir_edges.append((j, i, vals[i]))

        dir_edges.sort(key=lambda k: k[2], reverse=True) # sort edges by weight


        for i, _, p in dir_edges:
            if star_size[i] < k and p > 0:
                star_score[i] += p
                star_size[i] += 1

        
        print((star_score, star_size))
        return max(star_score)
    
    
