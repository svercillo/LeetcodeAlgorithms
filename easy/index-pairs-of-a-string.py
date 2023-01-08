def index_of(string, substring_start, match):
    n = len(string)

    i = substring_start
    while i < n:

        valid = True
        for j in range(len(match)):

            if i + j >= len(string):
                valid = False
                break
        
            if match[j] != string[i +j]:
                valid = False
                break
    
        if valid:
            return i

        i +=1

    return -1

class Solution:
    def indexPairs(self, text: str, words):
        res = []
        for w in words:
            index = index_of(text, 0, w)
            
            while index != -1:
                res.append([index, index + len(w)-1])
                index = index_of(text, index +1 , w)

        res.sort(key = lambda k: (k[0], k[1]))
                

        return res     
