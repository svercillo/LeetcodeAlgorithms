class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:        
        i = 0
        j = 1
        m = set({nums[0]})
        curr_val = nums[0]
        m_val = nums[0]
        while i < len(nums)-1:
            # print(m)
            if nums[j] not in m:
                
                m.add(nums[j])
                curr_val += nums[j]
                
                if j != len(nums) -1:
                    j += 1
                else:
                    i +=1

                    
            else:
                curr_val -= nums[i]
                m.remove(nums[i])
                i +=1
                            
            if curr_val > m_val:
                # print("sdfsdf", m, curr_val)
                m_val = curr_val

        
        return m_val
