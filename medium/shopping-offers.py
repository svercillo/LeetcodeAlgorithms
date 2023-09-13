class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
            n = len(prices)

            spec_map = {}
            for special in specials:
                spec_needs = tuple(special[:-1])
                if spec_needs not in spec_map:
                    spec_map[spec_needs] = special[-1]

                elif special[-1] < spec_map[spec_needs]:
                    spec_map[spec_needs] = special[-1]

            specials = [tuple(list(k) + [spec_map[k]]) for k in spec_map]

            print(specials)

            def dfs():
                print(needs)
                possible = []
                for special in specials:
                    can_use_special = True
                    for i in range(n):
                        if special[i] > needs[i]:
                            can_use_special = False
                            break

                    if not can_use_special:
                        continue
                    
                    for i in range(n):
                        needs[i] -= special[i]

                    special_price = special[-1]

                    possible.append(dfs() + special_price)

                    for i in range(n):
                        needs[i] += special[i]

                cost = 0
                for i in range(n): 
                    cost +=  needs[i] * prices[i]
                
                possible.append(cost)

                # print(possible)
                return min(possible)
            

            return dfs()

