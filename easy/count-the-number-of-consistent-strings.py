class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            valid = True
            for c in word:
                if c not in allowed:
                    valid = False
            if valid: count +=1
                
        return count
                
