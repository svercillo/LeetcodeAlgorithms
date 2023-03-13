class Solution:
    def splitNum(self, num: int) -> int:
        nums = []
        for c in str(num):
            nums.append(int(c))

        nums.sort()

        left = []
        right = []

        left_turn = True
        for e in nums:
            if left_turn:
                left.append(e)
            else:
                right.append(e)

            left_turn = not left_turn


        print(left, right)

        lstr = ""
        for c in left:
            lstr += str(c)


        rstr = ""
        for c in right: 
            rstr += str(c) 


        if lstr == "":
            lval = 0

        else:
            lval = int(lstr)
        
        if rstr == "":
            rval = 0
        else:
            rval = int(rstr)

        
        return lval + rval
