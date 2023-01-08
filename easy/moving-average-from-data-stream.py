from collections import deque

class MovingAverage:
    
    num = 0
    _sum = 0
    q = deque()
    

    def __init__(self, size: int):
        self.size = size
        
    def next(self, val: int) -> float:
        if self.num  < self.size:
            self.num += 1 
            self._sum += val
            self.q.append(val)
            return self._sum / self.num
        else:
            first = self.q.popleft()
            # print(first)
            self._sum -= first
            self._sum += val
            self.q.append(val)
            
            return self._sum / self.num
