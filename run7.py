from collections import defaultdict
import math
class Solution:
    def tallestBillboard(self, rods) -> int:
        dp = {0:0}

        for rod in rods:
            ndp = dp.copy()

            for diff in dp:
                shorter = dp[diff]  
                taller = shorter + diff

                # add to the taller side
                ndp[rod + taller - shorter] = max(dp[diff], ndp.get(rod+ taller - shorter, 0))

                # add to the smaller side 
                if rod + shorter <= taller:
                    ndp[taller - rod - shorter] = max(dp[diff] + rod, ndp.get(taller - rod - shorter, 0))
                else: # rod + shorer > taller
                    ndp[rod + shorter - taller] = max(dp[diff] + diff, ndp.get(rod + shorter - taller, 0))
            
            print(rod, ndp)
            dp = ndp

                
        return dp[0]
    
res =Solution().tallestBillboard([1,2,3,6])
print(res)