mport heapq
class StockPrice:

    class Price:
        def __init__(self, timestamp, price, compare_lt):
            self.timestamp = timestamp
            self.price = price
            self.compare_lt = compare_lt
            self.skip = False 
        def __lt__(self, other):
            if self.compare_lt[0]: 
                return self.price < other.price
            else:
                return self.price > other.price

        def __repr__(self):
            return f"Price<{self.timestamp}, {self.price}, {self.skip}>"

    def __init__(self):
        self.max = []
        self.min = []
        self.latest_price = 0
        self.latest_time = 0
        self.index = {}
        self.compare_lt = [True]

    def update(self, timestamp: int, price: int) -> None:

        if timestamp >= self.latest_time: 
            self.latest_price = price
            self.latest_time = timestamp

        price_obj = self.Price(timestamp, price, self.compare_lt)

        if timestamp in self.index:
            self.index[timestamp].skip = True
        
        self.compare_lt[0] = True
        heapq.heappush(self.min, price_obj)

        self.compare_lt[0] = False
        heapq.heappush(self.max, price_obj)

        self.index[timestamp] = price_obj # always update with latest value
    
    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        self.compare_lt[0] = False
        while self.max[0].skip: 
            heapq.heappop(self.max)

        return self.max[0].price
        
    def minimum(self) -> int:
        self.compare_lt[0] = True
        while self.min[0].skip:
            heapq.heappop(self.min)

        return self.min[0].price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
