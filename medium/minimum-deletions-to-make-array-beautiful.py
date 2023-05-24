class Solution:
    def minDeletion(self, nums: List[int]) -> int:

        cache = {}
        def min_deletions(index, is_even:bool, array_ind):
            k = (index, is_even)
            if k in cache:
                return cache[k]

            n = len(nums)
            if index == n:
                
                return 0 if array_ind % 2 == 0 else math.inf
            

            end_ind = index + 1

            while end_ind < n and nums[index] == nums[end_ind]:
                end_ind += 1

            num_occurences = end_ind - index

            smallest = math.inf
            if is_even:
                smallest = min(
                    smallest,
                    min_deletions(end_ind, False, array_ind + 1) + num_occurences - 1, # remove all but one occurence
                    min_deletions(end_ind, True, array_ind) + num_occurences # remove all occurences
                )
            else:
                if num_occurences >= 2:
                    smallest = min(
                        smallest,
                        min_deletions(end_ind, False, array_ind + 2) + num_occurences - 2
                    )

                smallest = min(
                    smallest,
                    min_deletions(end_ind, True, array_ind + 1) + num_occurences - 1
                )
                
            # print(index, is_even, smallest)
            cache[k] = smallest
            return smallest

        return min_deletions(0, True, 0)
