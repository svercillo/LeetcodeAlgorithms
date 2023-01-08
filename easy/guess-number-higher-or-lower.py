# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        while True:
            mid = (start + end) //2
            res = guess(mid)
            if res == 0:
                return mid

            if res == 1:
                start = mid +1
            else:
                end = mid -1
                
