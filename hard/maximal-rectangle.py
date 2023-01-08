class Solution:
    def maximalRectangle(self, matrix) -> int:
        n, m = len(matrix), len(matrix[0])


        msize = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                matrix[i][j] = matrix[i-1][j] + 1 if i != 0 and matrix[i][j] != 0 and matrix[i-1][j] > 0 else matrix[i][j]

            size = self.lra(matrix[i])
            msize = max(msize, size)

        return msize


    # largest rectangle area
    def lra(self, heights: List[int]) -> int: 
        class Node:
            def __init__(self, h, start):
                self.h = h
                self.start = start
                self.end = start

            def __repr__(self):
                return f"{self.h}: {self.start}"
        stack = [] 

        largest = 0
        for i, h in enumerate(heights):
            min_starting = i
            while len(stack) and stack[-1].h > h:
                top = stack.pop()
                if len(stack):
                    stack[-1].end = i

                top.end = i 
                largest = max(top.h * (top.end - top.start), largest)

                min_starting = min(min_starting, top.start)
            
            stack.append(Node(h, min_starting))

        while stack:
            top = stack.pop()

            top.end = len(heights)
            largest = max(top.h * (top.end - top.start), largest)

        return largest
