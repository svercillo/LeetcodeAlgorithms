class MRUQueue:

    def __init__(self, n: int):
        self.count = 0
        self.mruq = [[self.count, i] for i in range(1, n + 1)]
        

    def fetch(self, k: int) -> int:
        res = self.mruq[k-1][1]
        
        self.count += 1
        
        self.mruq[k-1][0] = self.count
        
        self.mruq.sort()
        
        return res
        
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
