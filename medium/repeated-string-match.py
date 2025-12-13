class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # abab
        # bababa
        na = len(a)
        nb = len(b)

        if na > nb:
            if b in a:
                return 1
            elif b in a + a: 
                return 2
            return -1


        if b in a:
            return 1 
        if b in a + a:
            return 2
        l = b.find(a)
        r = b.rfind(a) + na

        print(b[r:])

        if l == -1: 
            if b in a + a :
                return 2 
            else:
                return -1
        res = 0
        ai = 0

        for i in range(l, r):
            ai %= na
            if ai == 0:
                res += 1
            if b[i] != a[ai]:
                print( "sfailing ", l, r)
                return -1
            ai +=1 
    

        if r < nb:
            print(b[r:], "RIGHT side") 
            res += 1
            ai = 0
            for i in range(r, nb ): 
                if b[i] != a[ai]:
                    return -1   
                ai += 1
                
        if l > 0: 
            print(b[:l+1], ":LEF side") 
            res += 1
            ai = na -1
            for i in range(l-1, -1, -1):
                if b[i] != a[ai]:
                    return -1   

                ai -= 1

        

        # print(b[l:r], l,r)

        return res
            
        

        

            
    
