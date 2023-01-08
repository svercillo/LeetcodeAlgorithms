class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        index = []
        for i, c in enumerate(s): 
            if not c.isdigit():
                index.append(i)

        res = []
        n = pow(2, len(index))
        print(n)
        for i in range(n):
            scpy = [c for c in s]

        

            for j, ind in enumerate(index):
                print(i, pow(2,j))
                if i & pow(2, j) > 0:
                    # flip from lower to upper
                    if s[ind].isupper():
                        scpy[ind] = s[ind].lower()
                    else:
                        scpy[ind] = s[ind].upper()
            
            permu = ""
            for c in scpy:
                permu += c

            res.append(permu)
        return res
