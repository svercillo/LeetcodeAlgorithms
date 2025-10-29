# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        skip = set()
        possible = []
        for celeb in range(n):
            if celeb in skip:
                continue
            
            count = 0
            for person in range(n):
                print((celeb, person))
                if person == celeb:
                    continue

                if knows(person, celeb):
                    skip.add(person)
                    count += 1
                else:
                    break
            
            print("celeb", celeb, "count",  count)
            if count == n-1:
                possible.append(celeb)

        for celeb in possible:
            if celeb not in skip:
                skip = False
                for person in range(n): 
                    if celeb == person:
                        continue
                    if knows(celeb, person):
                        skip = True

                if not skip:
                    return celeb 

        return -1


