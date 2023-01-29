class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        last_digit = n-1
        for i in range(n -1):
            c = number[i]
            if c == digit:
                last_digit = i

                if int(number[i+1])  > int(digit):
                    print("SDFSDF")
                    return number[:i] + number[i+1:]
        if number[-1] == digit:
            last_digit = n-1
        return number[:last_digit]+ number[last_digit+1:]
