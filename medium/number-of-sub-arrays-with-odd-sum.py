class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        freq = [0, 0]

        count = 0
        presum = 0
        for s in arr:
            presum += s
            presum %= 2

            print(s, count)
            if presum == 0:
                v = freq[1]
            else:
                count += 1
                v = freq[0]

            count += v

            if presum % 2 == 0:
                freq[presum] += 1
            else:
                freq[presum] += 1

        return count  % (10 ** 9 + 7)
