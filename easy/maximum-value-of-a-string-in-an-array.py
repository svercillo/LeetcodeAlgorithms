class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mval = 0
        for s in strs:
            numeric = True
            for c in s:
                if not c.isdigit():
                    numeric = False
            mval = max(
                mval, 
                int(s) if numeric else len(s)
            )

        return mval
