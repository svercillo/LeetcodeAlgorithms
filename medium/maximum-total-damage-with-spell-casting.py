class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # reduce to freq list

        freq = {} 

        for p in power:
            if p not in freq:
                freq[p] = 0

            freq[p] += 1

        
        spells = sorted([

            (k, freq[k]) for k in freq
        ])
    
        n = len(spells)

        @cache
        def maxDamage(i):
            if i == n:
                return 0

            # don't take i
            resDontTake = maxDamage(i+ 1)

            next_ind = i + 1
            while next_ind < n and spells[next_ind][0] <= spells[i][0] + 2:
                next_ind += 1

            
            resTake = spells[i][0] * spells[i][1] + maxDamage(next_ind) 



            if resDontTake > resTake:
                return resDontTake
            else:
                return resTake

        return maxDamage(0)
