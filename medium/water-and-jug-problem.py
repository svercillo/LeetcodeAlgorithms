class Solution:
    def canMeasureWater(self, j1_cap: int, j2_cap: int, target: int) -> bool:

        if j1_cap > j2_cap:
            temp = j1_cap
            j1_cap = j2_cap
            j2_cap = temp

        visited = set()
        def dfs(j1, j2):
            nonlocal j1_cap, j2_cap, target
            print(j1, j2)
            
            if j1 == target or j2 == target or j1 + j2 == target:
                return True
            
            visited.add((j1, j2))
            if (j1_cap, j2) not in visited:
                if dfs(j1_cap, j2):
                    return True

            if (j1, j2_cap) not in visited:
                if dfs(j1, j2_cap):
                    return True

            if (0, j2) not in visited:
                if dfs(0, j2):
                    return True

            if (j1, 0) not in visited:
                if dfs(j1, 0):
                    return True


            # pour one jug into the other
            poured_out_of_j1 = min(j1, j2_cap - j2)
            if (j1 - poured_out_of_j1, j2 + poured_out_of_j1) not in visited:
                if dfs(j1 - poured_out_of_j1, j2 + poured_out_of_j1):
                    return True

            poured_out_of_j2 = min(j2, j1_cap - j1)
            if (j1+poured_out_of_j2, j2  -poured_out_of_j2) not in visited:
                if dfs(j1+poured_out_of_j2, j2  -poured_out_of_j2):
                    return True
            

        return dfs(0,0)

