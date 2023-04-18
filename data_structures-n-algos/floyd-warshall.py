import math

def min_cycle_length(vertices: list, edges: dict):
    n = len(vertices)
    
    vertex_map = {vertex : i for i, vertex in enumerate(vertices)} 

    dp = []
    for i in range(n):
        dp_matrix = []
        for j in range(n):
            dp_row = []
            for k in range(n):
                dp_row.append(math.inf)

            dp_matrix.append(dp_row)
        dp.append(dp_matrix)

    
    for _from, _to, l in edges:
        i, j = vertex_map[_from], vertex_map[_to]
        dp[i][j][0] = l # with no middle nodes, min distance is the length

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                dp[i][j][k] = min(
                    dp[i][j][k-1], # don't use the kth vertex
                    
                    dp[i][k][k-1] + dp[k][j][k-1] # use the kth vertex
                )

    min_cycle_length = math.inf
    for i in range(n):
        for j in range(n):
            if dp[i][j] != math.inf and dp[j][i] != math.inf:
                # if there is a path from i to j and j to i, a cycle is contained in this path

                if dp[i][j] == dp[j][i]:
                    # if the path from i to j and j to is the same length, this is a cycle
                    min_cycle_length = min(
                        min_cycle_length, 
                        dp[i][j][n-1]
                    )
            
    return min_cycle_length





    
vertices = ['A', 'B', 'C']
edges = [('A', 'B', 1), ('B', 'C', 1), ('C', 'A', 1)]
expected_output = 3

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B', 1), ('B', 'C', 1), ('C', 'D', 1), ('D', 'E', 1), ('E', 'A', 1), ('B', 'E', 1)]
expected_output = 3

vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 1), ('B', 'C', 1), ('C', 'D', 1), ('D', 'A', -5)]
expected_output = None

res = min_cycle_length(vertices, edges)


from pprint import pprint
pprint(res)

