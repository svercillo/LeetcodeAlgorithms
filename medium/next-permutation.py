class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        


        def swap( ai, bi):
            t = nums[ai]
            nums[ai] = nums[bi]
            nums[bi] = t

        def sortnums(start):
            count = 0 
            for i in range(start, (n - start) // 2 + start ):
                swap(start + count, len(nums)- 1 - count)
                count += 1

        def shiftdown(start):
            nonlocal n
            for i in range(n-1, start, -1):
                nums[i] = nums[i-1]
            
        def find(value, start):
            print(n-1, start, )
            for i in range(n-1, start-1, -1):
                print("SDFSDF", nums[i], value)
                if nums[i] > value: 
                    return i
            
            
            return -1


        print(nums)
        ind = n -2
        while ind >= 0 and nums[ind] >= nums[ind+ 1]:
            ind-= 1


        print(ind)

        if ind == -1:
            print( "fff")
            sortnums(0)
            return
        special = nums[ind]
        special_ind = ind

        




        find = find(special, special_ind+1)
    
        print(special, (nums[find], find))
        swap(special_ind, find)
        sortnums(special_ind+1)



        





        # nums[special_ind + 1] = special

        

      
