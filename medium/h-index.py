class Solution:
    def hIndex(self, arr: List[int]) -> int:
        

        arr.sort(reverse =True)
        mh = 0
        for i, e in enumerate(arr):

            mh = max(mh, min(i + 1, e))

        return mh
