import LinkedList

class Solution:
    def removeVowels(self, s: str) -> str:
        
        toremove = [] 

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ll = LinkedList()
        
        for c in s:
            if c not in vowels:
                ll.append(c)
                
        return str(ll)
