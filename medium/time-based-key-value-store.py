
class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.time_map:
            self.time_map[key] = []
            
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        
        
        if key not in self.time_map or len(self.time_map[key]) == 0:
            return ""
        
        n = len(self.time_map[key])
        
        
        def binary_search(array, target):
            if len(array) == 0:
                return None, False

            n = len(array)
            l, r = 0, n -1 

            while l <= r:
                m = (l + r) // 2

                if array[m][0] == target:
                    return m, True
                elif array[m][0] > target:
                    r = m -1 
                else:
                    l = m +1

            if l == n:
                return n -1, False
            
            while array[l][0] > target and l >= 0:
                l -=1 

            return l, False


        index, _ = binary_search(array = self.time_map[key], target = timestamp)
        
        # print(timestamp, self.time_map[key], index)
        if index == -1: 
            return ""
        
        else:
            return self.time_map[key][index][1]
        
        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
