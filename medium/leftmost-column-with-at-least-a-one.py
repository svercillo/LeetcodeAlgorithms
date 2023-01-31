# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, matrix: 'BinaryMatrix') -> int:
        n, m = matrix.dimensions()

        def find_leftmost_one(row):
            l, r = 0, m-1

            is_one = False
            while l <=r: 
                mid = (l+r) // 2
                value = matrix.get(row, mid)

                if value == 1:
                    r = mid -1
                else:
                    l = mid + 1

                if value == 1:
                    is_one = True
            
            return l, is_one

        
        furthest_left = m
        for i in range(n):
            ind, is_one = find_leftmost_one(i)

            if is_one:
                furthest_left = min(furthest_left, ind)

        return furthest_left if furthest_left != m else -1

