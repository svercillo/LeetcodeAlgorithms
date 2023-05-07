class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        words = [] 
        words.append(beginWord)
        for w in wordList:
            words.append(w)
        words.append(endWord)

        word_map = {}

        for i, e in enumerate(words):
            word_map[e] = i



        graph = []
        for i in range(len(words)):
            word = words[i]
            carr = [c for c in word]
            graph.append(set())

            for c_ind, character in enumerate(word):
                for offset in range(0, 26):
                    if chr(ord('a')  + offset) != character:
                        carr[c_ind] = chr(ord('a')  + offset)
                        neighbor = "".join(carr)    

                        if neighbor in word_map:
                            graph[i].add(word_map[neighbor])

                
                carr[c_ind] = character
        
        print(graph)

        # graph is built, now find shortest path from beginWord to endWord with BFS
        end_ind = len(words) -1
        q = [0]
        iterations = 0
        visited = set()
        while len(q):
            new_q = []
            for node in q:
                if node in visited:
                    continue

                visited.add(node)

                if node == end_ind:
                    print(node, words[node])
                    return iterations + 1

                for neigh in graph[node]:
                    new_q.append(neigh)
                
            q = new_q

            iterations += 1
        return 0
