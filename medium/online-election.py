class TopVotedCandidate:
    class Person:
        def __init__(self, id, num_votes, time):
            self.id = id
            self.num_votes = num_votes
            self.time = time
            self.duplicate = False

        def __lt__(self, other):
            if self.num_votes == other.num_votes:
                return self.time > other.time
            else:
                return self.num_votes > other.num_votes

        def __repr__(self):
            return f"Person<{self.id}, num:{self.num_votes}, time:{self.time}, d:{self.duplicate}>"

    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)
    
        people_map = {}
        heap = []

        top_person_at_time = []
        
        
        for i in range(n):
            person = persons[i]
            time = times[i]
            
            if person in people_map:
                obj = people_map[person]
                obj.duplicate = True
                
                new_obj = self.Person(person, obj.num_votes +1, i)
                heapq.heappush(heap, new_obj)
                people_map[person] = new_obj

            else:
                new_obj = self.Person(person, 1, i)

                people_map[person] = new_obj
                heapq.heappush(heap, new_obj)



            while heap[0].duplicate == True:
                heapq.heappop(heap)
            
            top_person_at_time.append(heap[0].id)
        
        self.top_person_at_time = top_person_at_time
        self.times = times
        

    def q(self, t: int) -> int:
        ind = bisect.bisect_right(self.times, t)
        
        return self.top_person_at_time[ind -1]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
