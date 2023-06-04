class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        n = len(people)
        people.sort()
        
        l, r = 0, n -1


        num_boats = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                l +=1
                r -=1
                num_boats += 1
            else:
                r -=1
                num_boats += 1

        
        return num_boats
