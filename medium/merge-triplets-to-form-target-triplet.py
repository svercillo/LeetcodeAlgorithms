class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        fv, sv, tv = False, False, False
        n = len(triplets)
        for i in range(n):
            f, s, t = triplets[i]


            if f == target[0] and s <= target[1] and t <= target[2]: 
                fv = True

            if f <= target[0] and s == target[1] and t <= target[2]: 
                sv = True 

            if f <= target[0] and s <= target[1] and t == target[2]: 
                tv = True

        return fv and sv and tv 

        
