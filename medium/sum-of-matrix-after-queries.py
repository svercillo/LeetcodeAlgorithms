class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        row_vals = defaultdict(lambda:(0,-1))
        col_vals = defaultdict(lambda:(0, -1))
        for i, (_type, index, val) in enumerate(queries):
            if _type == 0:
                container = row_vals
            else:
                container = col_vals

            container[index] = (val, i)


        rows_set = set()
        cols_set = set()
        total = 0

        for i in range(len(queries) -1, -1, -1):
            _type, index, val = queries[i]
            if _type == 0:
                _set = rows_set
                opp_set = cols_set
            else:
                _set = cols_set
                opp_set = rows_set

            if index in _set:
                continue
            _set.add(index)

            
            print(queries[i], val * (n - len(opp_set)))

            total += val * (n - len(opp_set))
            
        


        return total
                
