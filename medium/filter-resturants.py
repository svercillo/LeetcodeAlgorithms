class Solution:
    def filterRestaurants(self, rests: List[List[int]], isvf: int, maxprice: int, maxdist: int) -> List[int]:
        

        res = []
        for id, rating, vf, price, dist in rests: 

            if price > maxprice or dist > maxdist or (isvf and not vf):
                continue

            res.append((rating, id))
        
        res.sort(reverse = True)
        
        return [e[1] for e in res]
