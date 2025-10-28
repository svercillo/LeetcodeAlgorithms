class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        res_arr = []
        dp = defaultdict(int)

        for i in range(n1):
            for j in range(n2):
                multi = int(num1[i]) * int(num2[j])

                nzerosl = n1 - 1 -i
                nzerosr = n2 - 1 - j

                res = multi * 10 **(nzerosl + nzerosr)
                res_arr.append(res)

                for cind, c in enumerate(str(multi)[::-1]):
                    insrt_ind = cind + nzerosl + nzerosr
                    dp[insrt_ind] += int(c) 

                    while dp[insrt_ind] >= 10:
                        dp[insrt_ind+1] += 1
                        dp[insrt_ind] %= 10
                        insrt_ind += 1

        carr = []
        for ind in range(max(dp), -1, -1):
            carr.append(str(dp[ind]))
        

        return "".join(carr)


                


                
