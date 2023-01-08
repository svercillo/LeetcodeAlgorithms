class Solution:
    def findStrobogrammatic(self, n: int):
        char_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        res = [""]

        for i in range(n // 2):

            new_strs = []
            for c in char_map:
                if i == 0 and c == "0":
                    continue

                for string in res:
                    string = str(string)
                    string += c
                    new_strs.append(string)

            res = new_strs

        if n % 2 == 1:
            new_strs = []
            for c in char_map:
                if c == "6" or c == "9":
                    continue
                for string in res:
                    string = str(string)
                    string += c
                    new_strs.append(string)

            res = new_strs

        result = []
        while len(res) > 0:
            string = str(res.pop(0))
            for i in range(n // 2):
                string += char_map[string[n // 2 - 1 - i]]
            result.append(string)

        return result
