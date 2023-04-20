class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def longest_seq(ind1, ind2):
            m, n = len(text1), len(text2)

            if ind1 == m or ind2 == n:
                return 0

            mseq = 0
            if text1[ind1] == text2[ind2]:
                mseq = longest_seq(ind1+1, ind2+1) + 1

            mseq = max(
                longest_seq(ind1+ 1, ind2),
                mseq
            )

            mseq = max(
                longest_seq(ind1, ind2+1),
                mseq
            )

            return mseq


        return longest_seq(0, 0)
