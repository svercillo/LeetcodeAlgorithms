import math
class WordDistance:

    def __init__(self, wordsDict):
        
        self.map = {}
        for i,word in enumerate(wordsDict):
            if word not in self.map: 
                self.map[word] = []
            self.map[word].append(i)

    def shortest(self, w1: str, w2: str) -> int:
        
        def _get_min(word1, word2):
            p1, p2 = 0, 0
            
            n, m = len(self.map[word1]), len(self.map[word2])
            
            
            # print(self.map, word1, word2)
            smallest = math.inf
            while p2 < m:
                
                # print(self.map[word1][p1] , self.map[word2][p2])
                while p1 < n -1 and self.map[word1][p1] < self.map[word2][p2]:
                    smallest = min(smallest, abs(self.map[word1][p1] - self.map[word2][p2]))
                    
                    p1 += 1
                
                smallest = min(smallest, abs(self.map[word1][p1] - self.map[word2][p2]))
                p2 +=1 
            return smallest

        # print(_get_min(w2, w1))
            
        return min(_get_min(w1, w2), _get_min(w2, w1))
