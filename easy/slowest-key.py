class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        
        longest = releaseTimes[0]
        smallest_char = 'z'
        for i in range(1, len(keysPressed)):
            
            time = releaseTimes[i] - releaseTimes[i-1] 
            smallest_char = keysPressed[i] if keysPressed[i]  < smallest_char else smallest_char
        
            if time > longest: longest = time
        
        

        K = keysPressed[0] if releaseTimes[0] == longest else 'a'
        
        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i-1] 
            # print(time, longest)
            if time == longest and keysPressed[i] > K:
                # print(keysPressed[i])
                K = keysPressed[i]
                
        return K
