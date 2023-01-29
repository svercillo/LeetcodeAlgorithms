class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:

        n = len(nums)
        count = 0

        visited = set()
        for i in range(n):
            
            for j in range(i, n):
                num_divs = 0
                
                if tuple(nums[i:j+1]) in visited:
                    continue
                visited.add(tuple(nums[i:j+1]))


                for q in range(i, j+1):
                    if nums[q] % p == 0:
                        num_divs += 1

                        
                if num_divs <= k:
                    count +=1

            
        return count
