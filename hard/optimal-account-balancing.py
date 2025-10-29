from collections import defaultdict
class Solution:
    def minTransfers(self, trxns: List[List[int]]) -> int:
        ledger = [0] * 12
        for fr, to, amount in trxns:

            ledger[fr] -= amount
            ledger[to] += amount

        neg = []
        pos = []
        for bal in ledger:
            if bal < 0:
                neg.append(-bal)
            elif bal > 0:
                pos.append(bal)
        
        if not len(neg):
            return 0

        print(neg, pos)

        @cache
        def mintrans(remaining, negind, pos):
        
            if remaining == 0:
                if negind < len(neg) -1:
                    return mintrans(neg[negind+1], negind +1, tuple(pos))

                return 0

            # print(remaining, neg[negind:], pos)
            smallest = math.inf
            nvalue = neg[negind]


            smallest = math.inf
            for i, pvalue in enumerate(pos):
                npos = [e for j, e in enumerate(pos) if j != i]
                if pvalue > remaining:
                    npos.append(pvalue - remaining )

                    if negind < len(neg) -1:
                        smallest = min(mintrans(neg[negind+1], negind +1, tuple(npos)) + 1, smallest)
                else:
                    smallest = min(mintrans(remaining - pvalue, negind, tuple(npos)) + 1, smallest)

            print(smallest, pos, remaining, negind)

            return smallest
            
        return mintrans(neg[0], 0, tuple(pos))



