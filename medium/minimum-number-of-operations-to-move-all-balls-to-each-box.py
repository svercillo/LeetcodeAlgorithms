class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        # forward: sum of all distances to all balls 
        # for sum j - i * num balls infront 
        # 2  +  4 + 5 
        # 1 + 3 + 4
        # 0 + 2 + 3

        presums = []
        precount = []
        postsums = [0] * n
        postcount = [0] * n

        pres, prec = 0,0
        for i in range(n):
            if boxes[i] == "1":
                pres += i
                prec += 1

            precount.append(prec)
            presums.append(pres)


        posts, postc = 0, 0
        for i in range(n-1, -1, -1):
            if boxes[i] == "1":
                posts += n-1 - i
                postc += 1

            postcount[i] = postc
            postsums[i] = posts


        print(postsums, postcount)

        dp = [0] * n
        dp2 = [0] * n
        for i in range(n):
            num_ones_ahead = precount[-1] - precount[i]
            num_ones_behind = postcount[0] - postcount[i]

            print(i, num_ones_ahead, num_ones_behind) 

            dp[i] += (presums[-1] - presums[i]) - num_ones_ahead * i
            dp[i] += (postsums[0] - postsums[i]) - num_ones_behind * (n -1 - i)

            



        return dp
