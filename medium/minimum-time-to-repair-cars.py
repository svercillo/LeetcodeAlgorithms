class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:


        def max_num_of_minutes_is_valid(num_minutes, cars):            
            for r in ranks:
                n = math.floor((num_minutes / r) ** 0.5)
                cars -= n

            return cars <= 0
            

        l, r = 0, max(ranks) * cars ** 2
        while l <= r:

            print(l, r)
            m = (l + r) // 2
            
            if max_num_of_minutes_is_valid(m, cars): 
                r = m -1
            else:
                l = m + 1



        if max_num_of_minutes_is_valid(l-1, cars) and max_num_of_minutes_is_valid(l, cars):
            return l -1

        elif not max_num_of_minutes_is_valid(l-1, cars) and max_num_of_minutes_is_valid(l, cars):
            return l

        else:
            return l
            
