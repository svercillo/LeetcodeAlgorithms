def binary_search(array, target, l, r):
    if len(array) == 0:
        return None, False

    n = len(array)

    while l <= r:
        m = (l + r) // 2

        if array[m][0] == target:
            return m, True
        elif array[m][0] > target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n, False
    while array[l][0] > target and l >= 0:
        l -= 1

    l += 1

    print("FSDFSDF")
    return l, False


class Solution:
    def findRightInterval(self, intervals):

        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)

        intervals.sort(key=lambda k: k[0])
        # print(intervals)

        n = len(intervals)

        # res = [-1] * n
        res = [-1] * n
        for i in range(n - 1):
            end = intervals[i][1]

            j, _ = binary_search(intervals, end, i, n - 1)

            if j == n:
                res[intervals[i][2]] = -1
            else:
                # print(j)
                print(intervals[i], intervals[j])
                res[intervals[i][2]] = intervals[j][2]

        return res
