class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = {}
        for c in chars: 
            char_map[c] = 1 if c not in char_map else char_map[c] +1
            
        print(char_map)
        
        running = 0
        for w in words: 
            s = char_map.copy()
            
            invalid = False
            for c in w: 
                if c not in s:
                    invalid = True
                    break
                elif s[c] <= 0: 
                    invalid = True
                    break
                else:
                    s[c] -=1
            
            if not invalid: running += len(w)
        
        return running
