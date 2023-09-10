class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        

        @cache
        def minOps(i, group):
            n = len(nums)

            if i == n:
                return 0

            possible = []
            if nums[i] == group:
                possible.append(minOps(i + 1, group))
            elif nums[i] < group:
                possible.append(minOps(i + 1, group) + 1)
            else: # nums[i] > group
                # option 1: make nums[i] group
                possible.append(minOps(i + 1, group) + 1)

                # option 2: make group nums[i]
                possible.append(minOps(i + 1, nums[i]))
                

            return min(possible)
                


        

        return min(
            [
                minOps(0, 1),
                minOps(0, 2),
                minOps(0, 3)
            ]
        )
