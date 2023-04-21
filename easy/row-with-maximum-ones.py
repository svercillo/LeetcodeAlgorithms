class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:


        mcount = -1
        mcount_row = -1
        for i, row in enumerate(mat):
            count = 0
            for c in row:
                if c == 1:
                    count += 1

            if count > mcount:
                mcount = count
                mcount_row = i

        
        return (mcount_row, mcount)
