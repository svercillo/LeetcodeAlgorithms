class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix_ones = []
        pre_ones_sum = 0

        dp = {
            "1" : 0,
            "01" : 0,
            "0" : 0,
            "10" : 0
        }
        
        res = 0
        for c in s:
            if c == "0":
                res += dp["01"]
                dp["10"] += dp["1"]
                dp["0"] += 1
            else:
                res += dp["10"]
                dp["01"] += dp["0"]
                dp["1"] += 1

        return res 
