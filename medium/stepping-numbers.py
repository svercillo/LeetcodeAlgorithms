def copy(string):
    new_string = ""

    for c in string:
        new_string += c

    return new_string


class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        if high < 10:

            return [i for i in range(low, high + 1)]

        res = []

        q = [i for i in range(10)]  # integer q

        while len(q):

            new_q = []

            for num in q:

                if num in res:
                    continue

                print(num)
                if low <= num <= high:
                    res.append(num)

                elif num > high:
                    continue

                numstr = str(num)
                last_dig = int(numstr[-1])

                if last_dig > 0:
                    next_number = int(numstr + str(last_dig - 1))
                    new_q.append(next_number)

                if last_dig < 9:
                    next_number = int(numstr + str(last_dig + 1))
                    new_q.append(next_number)

            q = new_q

        return list(res)

    def bruteforce(self, low: int, high: int):

        res = []
        for num in range(low, high + 1):
            numstr = str(num)

            if len(numstr) == 1:
                res.append(num)

            else:
                valid = True
                for i in range(len(numstr) - 1):

                    if int(numstr[i + 1]) not in [
                        int(numstr[i]) + 1,
                        int(numstr[i]) - 1,
                    ]:
                        valid = False
                        break

                if valid:
                    res.append(num)

        return res


print("INSERT LOW, HIGH VALUES:")

low, high = int(input()), int(input())
print("\n")
res = Solution().countSteppingNumbers(low, high)

print(res)

test_res = Solution().bruteforce(low, high)
print(test_res)


def verify(actual, expected):

    assert len(actual) == len(expected)

    n = len(actual)

    for i in range(n):
        assert actual[i] == expected[i]


verify(res, test_res)

print("Test passed!")
