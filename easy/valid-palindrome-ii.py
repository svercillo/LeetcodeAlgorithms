class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        left = 0 
        right = n -1
        
        while left <= right and left < n and right >=0:
            
            if s[left] != s[right]:
                # try shifting left pointer by one
                
                l = left +1
                r = right
                
                left_shift_valid = True
                
                while l <= r and l < n and l >=0:
                    if s[l] != s[r]:
                        left_shift_valid = False
                        break
                    
                    l += 1
                    r -= 1
                        
                if not left_shift_valid:
                    
                    l = left
                    r = right -1 

                    while l <= r and l < n and l >=0:
                        if s[l] != s[r]:
                            return False
                        
                        l += 1
                        r -= 1
                break
            left +=1
            right -=1 
        return True
                
