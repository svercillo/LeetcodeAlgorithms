class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""

        slen = 0
        while num >= 2 ** slen:
            num -= 2 ** slen
            slen += 1

        rem = bin(num)[2:]
        return "0" * (slen - len(rem)) + rem


