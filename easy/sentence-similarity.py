class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        s1 = sentence1
        s2 = sentence2
        
        if len(s1) != len(s2):
            return False
        
        similar = {}
        
        for s, t in similarPairs:
            if s not in similar:
                similar[s] = set()
            if t not in similar:
                similar[t] = set()
            
            similar[s].add(t)
            similar[t].add(s)
            
        
        p1 = 0
        
        while p1 < len(s1):
            if s1[p1] != s2[p1] and (s2[p1] not in similar or s1[p1] not in similar[s2[p1]]):
                return False
            p1 += 1
                
        return True
            
