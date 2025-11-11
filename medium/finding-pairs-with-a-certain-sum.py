class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

        # print(self.freq1, self.freq2)

    def add(self, index: int, val: int) -> None:
        value = self.nums2[index]
        
        self.freq2[value] -=1
        self.freq2[value+ val] += 1

        self.nums2[index] += val

    def count(self, tot: int) -> int:

        # print(tot, self.freq1, self.freq2)
        res = 0
        for e in self.freq1:
            rem = tot -  e
            if rem  in self.freq2:
                res += self.freq2[rem] *  self.freq1[e]
    
        return res

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
