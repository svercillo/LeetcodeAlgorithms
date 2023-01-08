class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)


        def valid_string(string):
            if len(string) == 0 or len(string) > 3  or (len(string) > 1 and string[0] == "0"):
                return False
            value = int(string)
            if value > 255:
                return False
            
            return True

        res = []
        for i in range(0, 3):
            for j in range(i+1, i + 4):
                for k in range(j +1, j+ 4):

                    print(s[0:i+1] + "." + s[i+1: j +1] + "." + s[j+1:k+1] + "." + s[k+1:])
                    
                    if (
                        not valid_string(s[0:i+1])
                        or not valid_string(s[i+1: j +1])
                        or not valid_string(s[j+1:k+1])
                        or not valid_string(s[k+1:])
                    ):
                        continue

                    res.append(
                        s[0:i+1] + "." + s[i+1: j +1] + "." + s[j+1:k+1] + "." + s[k+1:]
                    )

        return res