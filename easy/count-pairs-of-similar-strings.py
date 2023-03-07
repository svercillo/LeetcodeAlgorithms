class Solution:
    def similarPairs(self, words: List[str]) -> int:
        word_set = []
        for word in words:
            word_set.append(set([c for c in word]))
            
        n = len(words)
        
        count = 0
        for i in range(n-1):
            for j in range(i + 1, n):
                if i == j: continue 
                    
                if word_set[i] == word_set[j]:
                    
                    count += 1
                    
        return count
            
            