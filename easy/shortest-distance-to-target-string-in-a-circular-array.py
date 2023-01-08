import math
class Solution:
    def closetTarget(self, words, target, startIndex): 
        target_inds = []
        for i, word in enumerate(words):
            if word == target:
                target_inds.append(i)

        if len(target_inds) == 0: 
            return -1
        

        shortest_dist = math.inf

        for ind in target_inds:            
            if ind >= startIndex:
                shortest_dist = min(
                    shortest_dist,
                    ind - startIndex,
                    len(words) - ind + startIndex
                )

            else:
                shortest_dist = min(
                    shortest_dist,
                    startIndex - ind,
                    len(words) - startIndex + ind
                )

        return shortest_dist
