class Solution:
    def invalidTransactions(self, array: List[str]) -> List[str]:
        trans = [] 
        for t in array:
            name, time, amount, city = t.split(",")

            time = int(time)
            amount = int(amount)


            trans.append((time, city, amount, name, t))

        trans.sort()

        n = len(trans)
        res = set()
        for i, tup in enumerate(trans):

            time, city, amount, name, t = tup

            if amount > 1000:
                res.add(i)
            j = i +1
            while j < n and trans[j][0] <= time + 60:
                if trans[j][1] != city and trans[j][3] == name:
                    res.add(i)
                    res.add(j)
                j += 1



        return [trans[ind][4] for ind in res]


            



        

            
            









        
