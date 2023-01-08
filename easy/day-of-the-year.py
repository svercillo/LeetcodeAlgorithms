from datetime import date
class Solution:
    def dayOfYear(self, d: str) -> int:
        arr = d.split("-")
        year = int(arr[0])
        month = int(arr[1])
        day = int(arr[2])
        d0 = date(year, 1, 1)
        
        d1 = date(year, month, day)
        
        delta = d1 - d0 
        return delta.days +1
