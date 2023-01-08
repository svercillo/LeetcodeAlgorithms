class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    
        visited = set()
        for word in words: 
            string = ""

            for c in word:
                string += morse[ord(c) - 97]

            
            visited.add(string)


        return len(visited)
            
