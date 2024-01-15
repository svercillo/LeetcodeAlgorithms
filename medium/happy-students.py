class Solution:
    def countWays(self, nums: List[int]) -> int:
        '''
        ideas:
            1. sort the array
            2. iterate throught the sorted array, if all were flipped before it, is it valid? if so count it
            3. this doesn't work because of duplicate values
        
        '''

        freq = {}
        for e in nums: 
            if e not in freq:
                freq[e] = 0
            freq[e] += 1

        student_reqs = sorted([v for v in freq])

        print(freq)
        print(student_reqs)

    

        num_ways = 0
        num_selected = 0
        for i in range(len(student_reqs)):
            curr_req = student_reqs[i]
            nstudents_with_req = freq[curr_req]

            if (
                num_selected + nstudents_with_req > curr_req 
                and num_selected + nstudents_with_req not in freq
            ):
                if i < len(student_reqs) -1:
                    if num_selected + nstudents_with_req >= student_reqs[i+1]:
                        num_selected += nstudents_with_req
                        continue
                    
                num_ways += 1
            num_selected += nstudents_with_req


        return num_ways + (1 if 0 not in freq else 0 )

