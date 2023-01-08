class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        if len(set(suits)) == 1:
            return "Flush"

        freq = {}
        for r in ranks:
            if r not in freq:
                freq[r] = 0
            freq[r] += 1

        
        val = sorted([freq[k] for k in freq], reverse=True)[0]

        if val >= 3:
            return "Three of a Kind"
        elif val == 2:
            return "Pair"
        else:
            return "High Card"
