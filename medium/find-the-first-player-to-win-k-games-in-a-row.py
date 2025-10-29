class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)

        i = 0
        won_first = 0
        while i < n:
            
            # count how many times ith guy wins
            j = i
            while j < n and skills[i] >= skills[j]:
                j += 1
                
            print(i, j)
            if j == n:
                return i # he beats all remaining guys
            
            if j - i -1  + won_first >= k:
                return i
            
            else:
                won_first = 1
                i = j
          
