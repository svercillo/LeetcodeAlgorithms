class Solution:
    class Node:
        def __init__(self, h, start):
            self.h = h
            self.start = start
            self.end = start

        def __repr__(self):
            return f"{self.h}: {self.start}"

    def largestRectangleArea(self, heights: List[int]) -> int:
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
            
            stack.append(self.Node(h, min_starting))

        while stack:
            top = stack.pop()

            top.end = len(heights)
            largest = max(top.h * (top.end - top.start), largest)

        return largest
