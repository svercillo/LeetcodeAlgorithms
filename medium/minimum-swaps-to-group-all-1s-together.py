class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)

        numones = 0
        for i in range(n):
            if data[i] == 1:
                numones += 1
    
        diff = set()
        for i in range(numones):
            if data[i] != 1:
                diff.add(i)

        minswaps = len(diff)
        if 0 in diff: 
            diff.remove(0)
        
        start, end = 1, numones
        while end < n:
            if data[end] != 1:
                diff.add(end)

            minswaps = min(minswaps, len(diff))
            
            if start in diff: 
                diff.remove(start)

            start += 1 
            end += 1

        return minswaps
