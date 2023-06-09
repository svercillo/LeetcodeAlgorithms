class Solution:
    def videoStitching(self, clips: List[List[int]], stop_time: int) -> int:


        
        n = len(clips)

        clips.sort(key = lambda k : k[0])

        if clips[0][0] != 0: 
            return -1

        j = 0
        max_start_ind = j
        max_end_ind = -1
        while j < n and clips[j][0] == clips[0][0]:
            if clips[j][1] > clips[max_start_ind][1]:
                max_start_ind = j
            j += 1


        
        count = 0
        while True:
            j = max_start_ind
            while j < n and clips[j][0] <= clips[max_start_ind][1]:
                if max_end_ind == -1 or clips[j][1] > clips[max_end_ind][1]:
                    max_end_ind = j
                j += 1

            count += 1

            if max_start_ind == max_end_ind or clips[max_start_ind][1] >= stop_time:
                break
                
            print(max_start_ind, max_end_ind)
            max_start_ind = max_end_ind
            

        if clips[max_end_ind][1] < stop_time:
            return -1
        else:
            return count
