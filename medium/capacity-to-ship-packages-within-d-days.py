class Solution:
    def capacity_is_valid(self, cap):
        ntrips = 1
        curr_cap = cap
        for w in self.weights:
            if w > cap: # empty ship cannot fit weight w
                return False

            if w <= curr_cap:
                curr_cap -= w
            else: # need to make another trip
                ntrips += 1
                curr_cap = cap - w


        print("ntrips", ntrips)

        return ntrips <= self.days

    def binary_search(self):
        lp = 1
        rp = 5 * 10 ** 4 * 500 + 1

        while lp <= rp: 
            m = (lp+rp) // 2
            if self.capacity_is_valid(m):
                rp = m - 1

            else:
                lp = m + 1

        
        while self.capacity_is_valid(lp):
            lp -= 1

        while not self.capacity_is_valid(lp):
            lp += 1

        return lp


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # days - 1 pointers such that the sum of any subarray is minimized

        self.weights = weights
        self.days = days
        

        print(self.capacity_is_valid(15))
        print(self.capacity_is_valid(16))

        # binary search answer
        return self.binary_search()
