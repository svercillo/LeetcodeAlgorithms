class Solution:
    def intToRoman(self, num: int) -> str:

        l = ["I", "V", "X", "L", "C", "D", "M"]
        v = [1, 5, 10, 50, 100, 500, 1000]

        i = len(v) - 1

        res = ""
        while num > 0 and i >= 0:
            print(i, num, v[i])

            while num >= v[i]:
                res += l[i]
                num -= v[i]

            if i == 1 or i == 2:
                while num >= v[i] - v[0]:
                    res += l[0] + l[i]
                    num -= v[i] - v[0]

            if i == 3 or i == 4:
                while num >= v[i] - v[2]:
                    res += l[2] + l[i]
                    num -= v[i] - v[2]

            if i == 5 or i == 6:
                while num >= v[i] - v[4]:
                    res += l[4] + l[i]
                    num -= v[i] - v[4]

            i -= 1
        return res
