class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank = set(bank)

        bank.add(startGene)

        genes = ['A', 'C', 'G', 'T']

        q = [startGene] 
        mutations= 0
        visited = set()
        while len(q):
            new_q = []
            for string in q:
                if string not in bank or string in visited: 
                    continue

                visited.add(string)

                if string == endGene:
                    return mutations
                
                current = [c for c in string]

                for i in range(8):
                    k = current[i]
                    
                    for gene in genes:
                        current[i] = gene

                        key = ""
                        for c in current:
                            key += c
                        new_q.append(key)
                    current[i] = k

            mutations += 1
            q = new_q

        return -1
