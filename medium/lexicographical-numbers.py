class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        

        res = []
        def recurse(previous):
            if previous > n:
                return
                
            res.append(previous)
            for dig in range(0, 10): 
                recurse(previous * 10 + dig)

        for e in range(1, 10):
            recurse(e)
        # print(res)

        return res
