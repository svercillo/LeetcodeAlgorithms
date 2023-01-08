class SnakeGame:

    charmap = {
        "U": [-1, 0],
        "D": [1, 0],
        "R" : [0 ,1],
        "L" : [0, -1]
    }
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        m = width
        n = height
        
        self.n = n
        self.m = m
        
        self.q = deque([(0,0)])
        self.has = set([(0,0)])
        self.food = food
        self.foodind = 0
    
    def move(self, direction: str) -> int:

        n = self.n
        m = self.m
            
        direct = self.charmap[direction]
        
        i, j = self.q[-1]
        ti, tj = i + direct[0], j + direct[1]
        
        if 0 <= ti < n and 0 <= tj < m:                
            if self.foodind < len(self.food):
                food = self.food[self.foodind]
                if (ti, tj) == tuple(food):
                    self.foodind += 1
                    if self.foodind > len(self.food):
                        return -1
                else:
                    coords = self.q.popleft()
                    self.has.remove(coords)
            else:
                coords = self.q.popleft()
                self.has.remove(coords)
                
                
            if (ti, tj) in self.has:
                return -1
            
            self.q.append((ti,tj))
            self.has.add((ti,tj))
        else:
            print("B")
            return -1
                
        return len(self.q) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
