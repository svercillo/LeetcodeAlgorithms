class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        
        banned = set(bannedWords)


        count = 0
        for word in message:
            if word in banned:
                count += 1 
            
            if count == 2:
                return True 
