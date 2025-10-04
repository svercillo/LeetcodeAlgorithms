class Node:
    def __init__(self, value, parent): 
        self.value = value
        self.children = {}
        self.parent = parent

class Trie:
    def __init__(self, words):
        self.head = Node("+", None)

        for word in words: 
            self.insert(word)

    def insert(self, word):
        node = self.head
        for c in word:
            if c in node.children: 
                node = node.children[c]
            else:
                newNode = Node(c, node)
                node.children[c] = newNode
                node = newNode
        node.children["*"] = True

    def remove(self, endnode):
        node = endnode

        if len(node.children) > 1:
            return
        else: 
            c = node.value
            node = node.parent
            
            node.children.pop(c)



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        n, m = len(board), len(board[0])

        dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]


        wordNodes = [] 
        visited = set()

        def constructword(node):
            res = []
            while node.value != "+":
                res.append(node.value)
                node = node.parent
            return "".join(res[::-1])
            

        def traverse(i, j, node):
            # each character can only be used once
            if (i,j) in visited:
                return

            visited.add((i, j))
            if "*" in node.children:
                wordNodes.append((node, (i, j)))
                trie.remove(node)
                
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if not (0<= ti < n and 0<=tj < m):
                    continue


                c = board[ti][tj] 

                if c in node.children:
                    traverse(ti, tj, node.children[c])
            visited.remove((i, j))

        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if c in trie.head.children: 
                    traverse(i, j, trie.head.children[c])  

        # print(wordNodes)

        return list(set([constructword(node) for node, coords in wordNodes]))
