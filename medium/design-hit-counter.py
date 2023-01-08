from bisect import *
class HitCounter:
    def __init__(self):
        self.counter = []

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)
        self.counter.sort()
        
    def getHits(self, timestamp: int) -> int:
        index = bisect_right(self.counter, timestamp)
        
       

        index = index -1 if index >= len(self.counter) else index
        
        count = 0
        while index >= 0 and timestamp - self.counter[index] < 300:
            count += 1
            index -=1
        
        
        return count
            
