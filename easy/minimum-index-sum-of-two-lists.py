class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        m1 = {e: i for i, e in enumerate(list1)}
        m2 = {e: i for i, e in enumerate(list2)}
        

        smallest_m = m1 if len(m1) <= len(m2) else m2
        

        common = []
        min_index_sum = math.inf
        for k in smallest_m:
            if k in m1 and k in m2:
                index_sum = m1[k] + m2[k]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    common = [k]
                elif index_sum == min_index_sum:
                    common.append(k)

        return common
