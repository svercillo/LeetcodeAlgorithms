class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        res = []
        for e in nums:
            cpy = e

            if e < 4:
                if e == 1:
                    res.append(0)
                elif e == 3:
                    res.append(1)
                else:
                    res.append(-1)
                continue



            digitInd = 0
            while cpy % 2 == 1:
                cpy = cpy // 2 
                digitInd += 1

            
            binary = list(bin(e)[2:])

            binary[len(binary) - (digitInd -1) -1 ] = "0"
            res.append(int("".join(binary), 2))



        return res
