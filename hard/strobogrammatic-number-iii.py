class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:

        chars = [0, 1, 6, 8, 9]
        chars_map = {0: 0, 1: 1, 6: 6, 8: 8, 9: 9}

        starting_chars = []
        for c in low:
            num = int(c)
            if num == 9:

                starting_chars.append(set([9]))
            else:
                running_set = set()
                for i, val in enumerate(chars):

                    if val >= num:
                        for j in range(i, len(chars)):
                            running_list.add(chars[j])
                        starting_chars.append(running_list)
                        break

        print(starting_chars)

        for i in range(len(high) - len(low)):
            running_list = set(chars)
            if i == 0:
                running_list.pop(0)
            starting_chars.append(running_list)

        for i in range(len(starting_chars) // 2):

            ind = len(starting_chars) - 1 - i


            pass


res = Solution().strobogrammaticInRange("50", "100")
print(res)
