class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.freq_count = {}

    def add(self, number: int) -> None:
        freq = self.freq
        freq_count = self.freq_count
    
        if number in freq:
            val = freq[number]
        else:
            val = 0

        if val > 0:
            freq_count[val] -= 1

        if val + 1 not in freq_count:
            freq_count[val+1] = 0
        
        freq_count[val+1] += 1
        freq[number] = val + 1
                
    def deleteOne(self, number: int) -> None:
        freq = self.freq
        freq_count = self.freq_count

        if number not in freq:
            return
        
        val = freq[number]
        freq[number] = val -1

        if freq[number] == 0:
            freq.pop(number)

        freq_count[val] -= 1

        if val -1 > 0:
            freq_count[val -1] += 1




        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count and self.freq_count[frequency] > 0
        
