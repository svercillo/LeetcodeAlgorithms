class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        @cache
        def getMax(i, started, skipped, nonempty=False):

            n = len(arr)
            if i == n:
                if nonempty:
                    return 0
                else: 
                    return -math.inf 
            if not started:
                return max(
                    getMax(i+1, 0, 0, False), # don't start
                    getMax(i+1, 1, 0, True) + arr[i], # don't skip
                    getMax(i+1, 1, 1, False) # skip 
                )
            else:
                res = []
                if skipped:
                    if nonempty: 
                        res.append(
                            arr[i] # stop subarary 
                        )

                    res.append(getMax(i+1, 1, 1, True) + arr[i]) # count this array)
                else:
                    if nonempty:
                        res.append(
                            arr[i]  # stop subarray
                        )

                    res.append(
                        max(
                            getMax(i+1, 1, 0, True) + arr[i], # don't skip
                            getMax(i+1, 1, 1, nonempty) # skip)
                        )
                    )

                return max(res)

        return getMax(0, 0, 0, False)

