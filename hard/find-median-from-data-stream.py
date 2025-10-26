class MedianFinder:

    def __init__(self):
        self.before = [math.inf]
        self.after = [math.inf]

        self.middle = None


    def addNum(self, num: int) -> None:
        before = self.before
        after = self.after

        # smallest number in after
        if num > after[0]:
            heapq.heappush(after, num)
        else: 
            heapq.heappush(before, -num)

        # rebalance
        nt = len(before) + len(after)


        # always put the extra in the before
        while len(before) < math.ceil(nt / 2):
            value = heapq.heappop(after)
            heapq.heappush(before, -value)

        while len(before) > math.ceil(nt / 2):
            value = -heapq.heappop(before)
            heapq.heappush(after, value)
            

            


        

    def findMedian(self) -> float:
        before = self.before
        after = self.after
        # print(sorted(before), sorted(after))

        nt = len(before) + len(after)

        if nt % 2 == 1:
            return -before[0]
        
        return (-before[0] + after[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
