class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        
        record = []
        
        for o in ops:
            if o == "+":
                record.append(record[len(record) -1] + record[len(record) -2])
            elif o =="C":
                record.pop()
            elif o == "D":
                record.append(record[len(record)-1] *2)
            else:
                record.append(int(o))
                
        return sum(record)
