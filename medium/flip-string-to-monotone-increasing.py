class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        prefix_zeros = [0 for _ in s]
        num_zeros = 0
        for i in range(n):
            if s[i] == '0':
                num_zeros += 1

                prefix_zeros[i] = num_zeros
                

        
        m_num_flips = math.inf
        
        for i in range(n):

            num_zeros_at_i = prefix_zeros[i]
            
            num_1_flips = i +1 - num_zeros_at_i
            num_0_flips = num_zeros - num_zeros_at_i

            total_flips = num_1_flips + num_0_flips

            if total_flips < m_num_flips:
                m_num_flips = total_flips


            # print(num_zeros_at_i, num_1_flips, num_0_flips)

        
        return min(m_num_flips, num_zeros, n - num_zeros)
