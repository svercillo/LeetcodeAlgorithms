class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:


        ''' 
        idea: n == 6 -> just try everything
        bfs
        '''
        nums2 = tuple(nums2)
        visited = set()
        q = [tuple(nums1)]
        
        iterations = 0
        while len(q): 
            nq = []
            for nums1 in q:

                if nums1 == nums2:
                    return iterations
                if nums1 in visited:
                    continue
                visited.add(nums1)


                for i in range(len(nums1)-1):
                    for j in range(i, len(nums1)):
                        subsection = nums1[i:j+1]
                        remaining = nums1[:i] + nums1[j+1:]

                        # print(subsection, remaining)
                        for insertionind in range(len(remaining)+ 1):
                            # print(insertionind)
                            # print(remaining[:insertionind], remaining[insertionind:])

                            new_nums1 = remaining[:insertionind] + subsection +  remaining[insertionind:]
                            # print(new_nums1)
                            nq.append(tuple(new_nums1))

            iterations += 1
            q = nq©leetcode
