class Solution:
    def getMaximumGenerated(self, n: int) -> int:



        @cache
        def nums(ind):
            
            
            if ind < 2:
                print(ind, ind)
                return ind
            

            if ind % 2 == 0:
                i = ind // 2
                print(ind, nums(i))
                return nums(i)
            else:
                i = (ind - 1) // 2

                print(ind, nums(i) + nums(i+1))
                return nums(i) + nums(i+1)

        
        mvalue = 0

        for i in range(n+1):
            mvalue = max(nums(i), mvalue)

        print(nums(3))
        return mvalue
