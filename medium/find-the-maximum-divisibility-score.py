class Solution:
    def addMinimum(self, word: str) -> int:
        
        valid_str = 'abc'
        vind = 2

        total = 0
        for i in range(len(word)):
            if word[i] == 'a':
                if vind == 0:
                    total += 2
                elif vind == 1:
                    total += 1
                else:
                    total += 0

                vind = 0

            elif word[i] == 'b':
                if vind == 1:
                    total += 2
                elif vind == 2:
                    total += 1
                else:
                    total += 0

                vind = 1
            else:
                if vind == 2:
                    total += 2
                elif vind == 0:
                    total += 1
                else:
                    total += 0

                vind = 2

        if vind == 0:
            total += 2
        elif vind == 1:
            total += 1
    
        return total
