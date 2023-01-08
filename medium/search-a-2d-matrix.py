def binary_search(array, target):
    if len(array) == 0:
        return None, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m] == target:
            return m, True
        elif array[m] > target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n , False
    while array[l] > target and l >= 0:
        l -= 1
    return l, False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        init_col = [matrix[i][0] for i in range(n)]
        
        row_ind, found = binary_search(init_col, target)
        
        if found: return True
        
        if row_ind == n:
            row_ind = n -1
            
        _, found = binary_search(matrix[row_ind], target)
        
        return found
