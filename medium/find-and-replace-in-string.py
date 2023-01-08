class Solution:
    def findReplaceString(self, s: str, indices, sources, targets) -> str:
        n = len(indices)
        
        indices, sources, targets = zip(*sorted(zip(indices, sources, targets), key = lambda k : k[0]))
 
        sind = 0
        indind = 0
        new_s = ""
        while sind < len(s) or indind < len(indices):
            startind = len(s)
            
            # if indind < len(indices):                
            #     startind = indices[indind]

            match = False
            while indind < len(indices) and indices[indind] == sind:
                if sind + len(sources[indind]) <= len(s):
                    match = True
                    for i in range(len(sources[indind])): 
                        if s[sind + i] != sources[indind][i]:
                            match = False
                    
                    if match:        
                        for i in range(len(targets[indind])):
                            new_s += targets[indind][i]
                        sind += len(sources[indind])

                indind += 1

            if not match:
                if sind < len(s):
                    new_s += s[sind]
                    sind += 1
        return new_s
