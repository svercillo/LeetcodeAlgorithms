class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)

        print(tokens)
        score = 0

        start = 0 
        end = n

        valid = True

        
        while True: 
            while start < end and power >= tokens[start]:
                score += 1
                power -= tokens[start]
                start += 1
            
            if score > 0 and end - start > 2:
                
                score -= 1
                power += tokens[end-1]
                tokens[end-1] = -1
                end -= 1

            else: 
                break

        return score
