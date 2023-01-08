class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = {}
        for w in words:
            for c in w:
                if c not in letters: 
                    letters[c] =1
                else: 
                    letters[c] +=1
        
        
        
        for c in letters:
            if letters[c] % len(words) !=0:
                return False
        
        return True
