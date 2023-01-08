class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        cost = 0
        prev = None
        
        n = len(colors)
        i = 0
        while i < n:
            c = colors[i] 
            if c == prev:
                largest = neededTime[i-1]
                largest_ind = i -1 

                j = i
                while j < n and colors [j] == prev:
                    if neededTime[j] > largest:
                        largest= neededTime[j]
                        largest_ind = j
                    j +=1 

                for c in range(i-1, j):
                    if c != largest_ind:
                        cost += neededTime[c]
                
                i = j - 1
            prev = c
            i += 1
        
        return cost
