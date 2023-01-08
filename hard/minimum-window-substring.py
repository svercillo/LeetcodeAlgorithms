import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        
        
        m = len(s)
        n = len(t)
        if n > m or s == "" or t == "": 
            return ""

        t_map = collections.Counter(t)
        s_map = { c : 0 for c in t_map}

        needed = set({c for c in t_map})
        extra = {}

        start = 0
        end = 0
        min_string = ""
        first = True
        while 0<= start and end <= m-1:
            
            if s[end] in needed:
                s_map[s[end]] += 1
                if s_map[s[end]] == t_map[s[end]]:
                    needed.remove(s[end])
            elif s[end] in t_map and first:
                # print("not good", s[end], s_map[s[end]], t_map[s[end]])
                if s_map[s[end]] >= t_map[s[end]]:
                    if s[end] not in extra:
                        extra[s[end]] = 1
                    else:
                        extra[s[end]] += 1

            if len(needed) != 0:
                # print("needed")
                if s[end] in t_map:
                    # print(s[end], s_map, t_map)

                    if s_map[s[end]] > t_map[s[end]]:
                        # print(s_map[s[end]],  t_map[s[end]], s[end])
                        if s[end] not in extra:
                            extra[s[end]] = 1
                        else:
                            extra[s[end]] += 1
                end += 1
                if end >= m:
                    return min_string
            else:
                first = False
                # print(s[start : end +1 ], extra)
                if min_string == "" or end+ 1 - start < len(min_string):
                    min_string = s[start : end +1]
                # break 
                if s[start] not in t_map:
                    start +=1

                else: 
                    if len(extra) ==0: 
                        end +=1 
                        if end <= m-1:
                            if s[end] in t_map:
                                if s[end] not in extra:
                                    extra[s[end]] = 1
                                else:
                                    extra[s[end]] +=1 
                        else: 
                            
                            break
                    
                    if s[start] in extra:
                        extra[s[start]] -=1
                        if extra[s[start]] == 0:
                            extra.pop(s[start])
                        start +=1
                    else:
                        end +=1 
                        if end >= m:
                            end -= 1
                            break
                        if s[end] in t_map:
                            if s[end] not in extra:
                                extra[s[end]] = 1
                            else:
                                extra[s[end]] +=1 

        return min_string
                
