class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        word_set = set({})
        pat_to_word = {}
        for i in range(len(words)):
            word = words[i]
            c = pattern[i]
            
            if c in pat_to_word:
                if word != pat_to_word[c]:
                    return False
            else:
                if word not in word_set:
                    word_set.add(word)
                    pat_to_word[c] = word
                    
                else:
                    return False
                
        return True
                
                
                
            
            
            
