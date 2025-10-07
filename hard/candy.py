class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if len(set(ratings)) == 1:
            return len(ratings)
        print(n)
        if n ==1: 
            return 1


        def compress(ratings):  
            n = len(ratings )
            freq = []
            i = 0
            res = []
            while i < n:
                j = i    
                res.append(ratings[i])
                while j < n and ratings[j] == ratings[i]:
                    j += 1

                freq.append(j - i)
                i = j

            return res
        
        
        def findlocalmin(ratings):
            n = len(ratings)
            localmins = []
            res = [] 
            for i, e in enumerate(ratings):
                if i == 0: 
                    if ratings[0]< ratings[1]:
                        res.append(e)
                elif i == n -1:
                    if ratings[-1] < ratings[-2]:
                        res.append(e)
                elif ratings[i-1] > ratings[i] < ratings[i+1]: 
                    # if local min 
                    res.append(e)
            return res

        def indmapping(ratings):
            mapping = {}
            for i, e in enumerate(ratings):
                if e not in mapping:
                    mapping[e] = []
                mapping[e].append(i)
            return mapping
        


        compressed_ratings  = compress(ratings)
        localmins = list(set(findlocalmin(compressed_ratings)))
        heapq.heapify(localmins)

        mappings = indmapping(ratings)


        # print(ratings, freq)        
        print("localmins", localmins)
        print(mappings)

        mr = min(ratings)
        res = [1] * len(ratings) 
        dirs = [-1, 1]
        while len(localmins):
            smallest = heapq.heappop(localmins)
            q = [(e, 1) for e in mappings[smallest]]

            print("sdfsdfs", smallest)


            while len(q):
                nq = set()
                
                for ind, count in q:
                    print(ind, count)
                    res[ind] = max(res[ind], count)
                    for move in dirs:

                        tind = ind
                        while 0 <= tind + move < len(ratings) and ratings[tind] == ratings[tind + move]:
                            tind += move
                            print("SDFSDFS", tind) 
                            count = 1                  
                        
                        tind += move

                        if not (0 <= tind < len(ratings)):
                            continue
                        
                        if ratings[ind] > ratings[tind]:
                            continue


                        print("putting in ", tind, ind, count+ 1)

                        nq.add((tind, count + 1))

                q = list(nq)
                print(q)
            

        # print(res)
        # print(ratings)


        return sum(res)


            



        



    

