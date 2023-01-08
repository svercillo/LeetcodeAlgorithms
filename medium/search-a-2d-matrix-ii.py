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
        return n - 1, False
    while array[l] > target and l >= 0:
        l -= 1

    return l, False
class Solution:
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            j, found = binary_search(matrix[i], target)
            
            if found: return True
        else:
            return False
