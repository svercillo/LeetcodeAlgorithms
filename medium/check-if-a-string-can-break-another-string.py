class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        def can_break(s1, s2):
            freq1 = [0] * 26
            
            for c in s1:
                ind = ord(c) - ord('a')
                freq1[ind] += 1

            for c in s2:
                ind = ord(c) - ord('a')


                found_greater_char = False 
                while ind < 26:
                    if freq1[ind] > 0:
                        freq1[ind] -= 1 
                        found_greater_char = True
                        break
                    ind += 1

                if not found_greater_char:
                    return False
            
            return True
                
        return can_break(s1, s2 ) or can_break(s2, s1)
