class StockSpanner:

    def __init__(self):
        self.minHeap = []
        self.ind = 0
        

    def next(self, price: int) -> int:
        
        minHeap = self.minHeap
    
        while len(minHeap) and minHeap[-1][0] <= price:
            _p = minHeap.pop()    

        if len(minHeap):
            numDays = self.ind - minHeap[-1][1]
        else:
            numDays = self.ind + 1

        minHeap.append((price, self.ind))


        self.ind += 1
        return numDays
        
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
