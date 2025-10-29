from collections import deque

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        needed_songs = goal
        
        # these three are unique to a function run
        time_to_deque = []
        qfreq = {}
        used = set()

        for i in range(n): 
            time_to_deque.append(None)
        for i in range(0, n+1):
            qfreq[i] = 0

        # how do i know that i've used up all the song
        def numPlaylists(goal):
            nonlocal n, k, needed_songs
            curr_time = needed_songs - goal
            if goal == 0:
                for e in qfreq:
                    if qfreq[e] == 0:
                        return 0
                return 1
            
            for ind in range(0, n + 1):
                # song has already been played recently
                # evict elements from the q that are not recently played
                if qfreq[ind] > 0:
                    continue
                
                used.add(ind)
                if curr_time + k < needed_songs:
                    time_to_deque[curr_time + k] = ind
            

        return numPlaylists(goal)

res = Solution().numMusicPlaylists(n = 3, goal = 3, k = 1)
# res = Solution().numMusicPlaylists(n = 2, goal = 3, k = 0)
print("\nsolution", res)