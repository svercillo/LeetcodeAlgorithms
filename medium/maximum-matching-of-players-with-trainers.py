class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        heapq.heapify(players)
        heapq.heapify(trainers)


        count = 0

        while len(players) and len(trainers):
            while len(trainers) and trainers[0] < players[0]:
                heapq.heappop(trainers)
            
            if len(trainers):
                heapq.heappop(trainers)
                heapq.heappop(players)
                count += 1
            
        return count 

            
