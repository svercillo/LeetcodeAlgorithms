class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        largest_mul = [0] * n

        largest_mul[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            largest_mul[i] = max(nums[i], largest_mul[i+1])

        
        # print(largest_mul)
        m_profit = 0

        largest = -1
        for i in range(n-1):
            
            profit = (largest - nums[i]) * largest_mul[i+1]
            m_profit = max(m_profit, profit)

            # print(largest, nums[i], largest_mul[i])

            if nums[i] > largest:
                largest = nums[i]

        return m_profit 



            

            

            

