class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ['+', '-', '*', '/']
        
        def all_possible_ways(start, end, cards):
            if start == end-1:
                return [cards[start]]
                

            res = []
            for split in range(start + 1, end):

                first = all_possible_ways(start, split, cards)
                second = all_possible_ways(split, end, cards)
                
                
                for sub1 in first: 
                    for sub2 in second:
                        for op in ops:
                            if op == "+":
                                res.append(sub1 + sub2)
                            if op == "-":
                                res.append(sub1 - sub2)
                            elif op == "*":
                                res.append(sub1 * sub2)
                            elif op == "/":
                                if sub2 != 0:
                                    res.append(sub1 / sub2)

            return res
                  
        def get_arrangements(cards):
            if len(cards) == 1:
                return [[cards[0]]]

            res = []
            for i in range(len(cards)):
                cpy = []
                for j in range(len(cards)):
                    if i == j:  
                        continue
                    cpy.append(cards[j])

                possible = get_arrangements(cpy)
                for poss in possible:
                    poss_cpy = poss.copy()
                    poss_cpy.append(cards[i])
                    res.append(poss_cpy)

            return res

        arrangements = get_arrangements(cards)


        for arr in arrangements:
            for val in all_possible_ways(0, 4, arr):
                if abs(val - 24) < 1/1000: 
                    return True


        return False
