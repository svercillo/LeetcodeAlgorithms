class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def is_index_this_value(n, k, value):
            if n == 1:
                return value == 0
                
            if value == 0:
                if k % 2 == 0:
                    return is_index_this_value(n-1, k // 2, 0)
                else:
                    return is_index_this_value(n-1, k // 2, 1)

            else:
                if k % 2 == 0:
                    return is_index_this_value(n-1, k // 2, 1)
                else:
                    return is_index_this_value(n-1, k // 2, 0)


        if is_index_this_value(n, k-1, 1):
            return 1
        else:
            return 0





