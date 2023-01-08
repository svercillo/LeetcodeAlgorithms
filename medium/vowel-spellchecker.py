import math
from collections import OrderedDict

class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = OrderedDict({'a': None, 'e': None, 'i': None, 'o':None, 'u':None})
        caps_map = {}

        total = set({})
        
        ind_map = {}
        for i, w  in enumerate(wordlist): 
            total.add(w)
            low = w.lower()
            if low not in caps_map: 
                caps_map[low] = w
            
            if w not in ind_map:
                ind_map[w] = i 
            

        # print(ind_map)
                
        res = []
        for q in queries: 
            if q in total:
                res.append(q)
                continue
            q = [c.lower() for c in  q]
            
            low = ''.join(q)
            if low in caps_map:
                res.append(caps_map[low])
            else:
                
                found = False
                i =0
                v_inds = [] 
                for i in range(len(q)):
                    if q[i] in vowels: 
                        v_inds.append(i)
                
                

                def recurse(i, string, v_inds, found):

                    if i == len(v_inds): 
                        return 
                    
                    for v in vowels:
                        new_string = string[:v_inds[i]] + v + string[v_inds[i]+1:]
                        
                        if new_string in caps_map:

                            # print(caps_map[new_string])
                            if ind_map[caps_map[new_string]] < found[0]:
                                found[0] = ind_map[caps_map[new_string]]
                                found[1] = caps_map[new_string]
                                


                        recurse(i +1, new_string, v_inds, found)


                
                found_string = [math.inf, None]
                recurse(0, low, v_inds, found_string)
                
                

                if not found and found_string[0] == math.inf: 
                    res.append("")
                else: 
                    res.append(found_string[1])
                    
        return res
