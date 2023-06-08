class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        class Team:
            def __init__(self, scores, name):
                self.name = name
                self.scores = scores

            def compare(self, other, position):
                if position == len(self.scores):
                    return self.name < other.name
                elif self.scores[position] == other.scores[position]: 
                    return self.compare(other, position + 1)
                else:
                    return self.scores[position] > other.scores[position]

            def __lt__(self, other):
                return self.compare(other, 0)

        freq = {}
        for vote in votes:
            for i, c in enumerate(vote):
                if c not in freq:
                    freq[c] = Team([0] * len(votes[0]), c)

                freq[c].scores[i] += 1
                
        sorted_arr = sorted([freq[k] for k in freq])

        return "".join([team.name for team in sorted_arr])
            
        
