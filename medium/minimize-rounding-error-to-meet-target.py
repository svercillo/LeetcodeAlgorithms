class Solution:
    def minimizeError(self, prices_str: List[str], target: int) -> str:
        
        prices = [ float(p) for p in prices_str]

        n = len(prices)
        smallest = 0
    
        possible_flips = 0
        for p in prices:
            smallest += math.floor(p)


            possible_flips += 1
            if math.floor(p) == math.ceil(p):
                possible_flips -=1


        largest = smallest + possible_flips


        if not (smallest <= target <= largest): 
            return "-1"

        
        prices_dec = [int(k.split(".")[1]) for k in prices_str]
        prices_dec.sort(reverse=True)

        total = sum(prices_dec)
        
        num_ceils = target - smallest
    
        count = 0
        while count < num_ceils:
            dec = prices_dec[count]
            total -= dec 
            total += 1000 - dec

            dec = prices_dec[count]
            count += 1
            

        total /= 1000 
        return "{:.3f}".format(total)

