class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.buff = 0
    
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.buff += 1 
            if self.buff >= self.k:
                return True
            else:
                return False
        else:
            self.buff = 0
            return False
        
