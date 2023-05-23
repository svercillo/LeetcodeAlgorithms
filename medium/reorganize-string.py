class Solution:
    def reorganizeString(self, s: str) -> str:
        class Letter:
            def __init__(self, letter, freq):
                self.letter = letter
                self.freq = freq

            def __lt__(self, other):
                return self.freq > other.freq

            def __repr__(self):
                return f"Letter<{self.letter}, {self.freq}>"

        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1


        heap = []
        for c in freq:
            heapq.heappush(heap, Letter(c, freq[c]))



        res = []
        last = None
        while len(heap):
            # print(heap, last)
            letter = heapq.heappop(heap)

            if last == letter.letter:
                if not len(heap):
                    return ""
                else: 
                    print("SDFsdf", heap)
                    second_letter = heapq.heappop(heap)
                    heapq.heappush(heap, letter)
                    letter = second_letter

            res.append(letter.letter)
            letter.freq -= 1
            
            if letter.freq:
                # print("pushing letter", letter)
                heapq.heappush(heap, letter)
                # print(heap[0])
            
            last = letter.letter

            # print(heap)
        
        return "".join(res)
            
