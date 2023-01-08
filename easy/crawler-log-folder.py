class Solution:
    def minOperations(self, logs: List[str]) -> int:
        pos = 0
        for l in logs:
            if l.find("..") != -1:
                if pos >0:
                    pos -=1 
            elif l.find(".") != -1:
                pos += 0
            else: 
                pos +=1 
                
        return pos
