# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    # Write Python 3 code in this online editor and run it.


    def binary_search(self, len_arr, start_ind): # start_ind is the ind of first element
            print(len_arr, start_ind, isBadVersion(start_ind + len_arr //2))
            if len_arr  ==1: 
                return int(start_ind)
            if isBadVersion(start_ind + len_arr//2):
                return self.binary_search(len_arr //2, start_ind)
            else: 
                return self.binary_search(len_arr //2, start_ind + len_arr // 2)



    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = self.binary_search(n+1, 0)
        while not isBadVersion(res):
            res +=1 
            
        return res
