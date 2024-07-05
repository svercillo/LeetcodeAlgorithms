class Solution:
    def maxProfit(self, prices) -> int:

        n = len(prices)
        int1 = None
        int2 = None
        bottom_after_int2 = None

        max_profit = 0
        for p in prices:
            print("price ", p)
            if int1 is None:
                int1 = [p, None]
            elif int1[1] is None:
                if p <= int1[0]: 
                    int1[0] = p # decreasing
                else:
                    int1[1] = p
            elif int2 is None: 
                if p >= int1[1]:
                    int1[1] = p
                else:
                    int2 = [p, None]
            elif int2[1] is None:
                if p <= int2[0]:
                    int2[0] = p
                else:
                    int2[1] = p
            elif bottom_after_int2 is None: 
                if p >= int2[1]:
                    int2[1] = p
                else:
                    bottom_after_int2 = p
            else:
                
                if p <= bottom_after_int2:
                    bottom_after_int2 = p # decreasing
                else:
                    top_after_int2 = p
                    diff3 = top_after_int2 - bottom_after_int2
                    curr_prof = int2[1] - int2[0] + int1[1] - int1[0]

                    if int1[0] < int2[0]:
                        print("     price ", p)
                        if int1[1] < int2[1]:
                            # combine the two intervals as it's optimal
                            combined_diff = int2[1] - int1[0]
                            
                            if combined_diff + diff3 > curr_prof:
                                int1 = [int1[0], int2[1]]
                                int2 = [bottom_after_int2, top_after_int2]
                                bottom_after_int2 = None

                        else:
                            # don't use the second one at all, only the first
                            combined_diff = int1[1] - int1[0]

                            if combined_diff + diff3 > curr_prof:
                                int2 = [bottom_after_int2, top_after_int2]
                                bottom_after_int2 = None
                    else:
                        if int1[1] - int1[0] > int2[1] - int2[0]:
                            # only use the first interval
                            combined_diff = int1[1] - int1[0]

                            if combined_diff + diff3 > curr_prof:
                                int2 = [bottom_after_int2, top_after_int2]
                                bottom_after_int2 = None
                        else:
                            # only use the second interval
                            combined_diff = int2[1] - int2[0]

                            if combined_diff + diff3 > curr_prof:
                                int1 = int2
                                int2 = [bottom_after_int2, top_after_int2]
                                bottom_after_int2 = None

            
            curr_profit = 0
            if int1 is not None and int2 is not None and int2[1] is not None:
                curr_profit = int2[1] - int2[0] + int1[1] - int1[0]
            elif int1 and int1[1] is not None:
                curr_profit = int1[1] - int1[0]


            print(int1, int2, bottom_after_int2)

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit
        
res = Solution().maxProfit(
    [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]
)

print(res)