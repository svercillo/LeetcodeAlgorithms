class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        


        bright = bin(right)[2:]
        bleft= bin(left)[2:]

        if len(bright) > len(bleft):
            print("SDfsdfsdf")
            return 0


        res = 0
        for i in range(len(bleft)):

            print(bleft, bright)
            if bleft[i] == '0' and bleft[i] != bright[i]:
                break 
            
            print("sdfsdf", bleft[i], i)
            if bleft[i] == '1':
                res += 2 ** (len(bleft) - 1 - i) 

        
        if i == len(bleft):
            return 0
        

        return res
