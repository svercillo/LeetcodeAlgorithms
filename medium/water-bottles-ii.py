class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        def maxDrunk(numBottles, numEx):
            if numBottles == 0:
                return 0

            res = 0
            if numBottles >= numEx:
                # drink numEx bottles and trade one in
                res = max(res, maxDrunk(numBottles - numEx + 1, numEx + 1) + numEx)
            res = max(res, maxDrunk(0, -1) + numBottles)

            return res 

        return maxDrunk(numBottles, numExchange)


