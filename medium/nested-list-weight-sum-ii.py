class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        dp = []

        max_depth = 0
        def dfs(array, depth):
            nonlocal max_depth


            for e in array:
                if e.isInteger():
                    
                    dp.append((e.getInteger(), depth))
                    max_depth = max(max_depth, depth)
                else:
                    max_depth = max(max_depth, depth)
                    dfs(e.getList(), depth +1)
        dfs(nestedList, 1)

        
        print(dp, max_depth)
        res = 0
        for w, depth in dp:
            res += w * (max_depth - depth + 1)
        return res
