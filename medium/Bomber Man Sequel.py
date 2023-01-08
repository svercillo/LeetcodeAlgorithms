class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
    
        dp = []
        rowkills = []
        for i in range(n):
            groupkills = [0] * m
            kills = 0
            start  = 0
            for k in range(m):
                if matrix[i][k] == 2:
                    kills += 1
                elif matrix[i][k] == 1:
    
                    print(start, k)
                    for p in range(start, k):
                        groupkills[p] = kills
                    start = k +1
                    kills = 0
            
            while start <= k:
                groupkills[start] = kills
                start += 1 

            rowkills.append(groupkills)

        print("row", rowkills)

        colkills = []
        for j in range(m):
            groupkills = [0] * n
            kills = 0
            start  = 0
            for k in range(n):
                if matrix[k][j] == 2:
                    kills += 1
                elif matrix[k][j] == 1:
                    
                    for p in range(start, k):
                        groupkills[p] = kills
                    start = k +1
                    kills = 0
            
            while start <= k:
                groupkills[start] = kills
                start += 1 

            colkills.append(groupkills)
        print("col", colkills)


        _max = 0

        for i in range(n):
            for j in range(m):
                _sum = 0
                if matrix[i][j] == 0:
                    
                    _sum += rowkills[i][j]
                    _sum += colkills[j][i]
                    
                    _max = max(_sum, _max)

        return _max
