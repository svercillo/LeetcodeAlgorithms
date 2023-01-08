class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        _set = set({})

        if  k >= len(s):
            return False
        assert k < len(s)
        for i in range(0, len(s)-k+1):

            ele = s[i:i+k]
            _set.add(s[i:i+k])

        

        

        # print(_set)
        num_req = pow(2, k)

        return len(_set) == num_req
