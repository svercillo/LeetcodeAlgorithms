class Solution:
    def stringSequence(self, target: str) -> List[str]:
        endInd = len(target) -1
        currLetter = ord(target[-1])


        res = []
        while endInd >= 0:
            if currLetter == 96:
                currLetter = ord(target[endInd])

            while currLetter >= 97: 
                res.append(target[:endInd] + chr(currLetter))
                currLetter -= 1
            
            endInd -= 1
                
        return res[::-1 ]


            
            
