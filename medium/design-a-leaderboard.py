class Leaderboard:


    '''
    idea: 
        two separate queues:
            1. top K elements sorted with smallest first
            2. all other elements 
        keep node map
    '''

    class Node:
        def __init__(self, playerId, score):
            self.playerId = playerId
            self.score = score
            self.invalid = False

        def __lt__(self, other):
            if self.invalid: 
                return False
            elif other.invalid:
                return True
            return self.score > other.score

    def __init__(self):
        self.node_map = {}
        self.q = []


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.node_map:
            node = self.Node(playerId, score)
            self.node_map[playerId] = node
            heapq.heappush(self.q, node)
        else:
            node = self.node_map[playerId]
            node.invalid = True
            new_node = self.Node(playerId, score + node.score)
            self.node_map[playerId] = new_node
            heapq.heappush(self.q, new_node)
            
    def top(self, K: int) -> int:
        elements = heapq.nsmallest(K, self.q)

        top_score = 0
        for node in elements:
            if node.invalid:
                continue
            top_score += node.score

        return top_score



    def reset(self, playerId: int) -> None:
        node = self.node_map[playerId]
        node.invalid = True
        new_node = self.Node(playerId, 0)
        self.node_map[playerId] = new_node
        heapq.heappush(self.q, new_node)
    

        



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
