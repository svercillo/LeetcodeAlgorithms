class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        def remaining(number, target):

            if len(number) >= len(target):
                return "-1"


            i =0
            while i < len(number):
                if number[i] != target[i]:
                    return "-1"

                i += 1 
            return target[len(number):]

        total = 0
        freq = {}
        for i, num in enumerate(nums):
            if num not in freq: 
                freq[num] = 0
            freq[num] += 1

        for i, num in enumerate(nums):

            # freq[num] -= 1
            # if freq[num] == 0:
            #     freq.pop(num)


            rem_str = remaining(num, target)
            if rem_str in freq:
                if rem_str == num:
                    total += freq[rem_str] - 1
                else:
                    total += freq[rem_str]
        return total 
