class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        first_to_change = -1
        for i, c in enumerate(palindrome):
            if c != 'a' and first_to_change == -1 and (n % 2 == 0 or i != n // 2 ):

                first_to_change = i


        if first_to_change != -1:
            cpy = [c for c in palindrome]
            cpy[first_to_change] = 'a'
            return "".join(cpy)
        else:
            if n == 1:
                return ""
            else:
                cpy = [c for c in palindrome]
                cpy[-1]  = 'b'

                return "".join(cpy)
