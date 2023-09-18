class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        def minIncrs(node):
            nonlocal n
            left = 2 * node + 1
            right = 2 * node + 2

            if left >= n: 
                return 0

            total_incrs = 0 
            total_incrs += minIncrs(left)
            total_incrs += minIncrs(right)

            total_incrs += abs(cost[left] - cost[right])
            cost[node] += max(cost[left], cost[right])
            
            return total_incrs

        return minIncrs(0) 
            



