
class Trie:

    class Node:
        def __init__(self, letter, prev=None):
            self.letter = letter
            self.next = {}
            self.prev = prev


    def __init__(self):
        self.head = self.Node("%")

    def add_word(self, word):
        node = self.head
        for c in word:
            if c not in node.next:
                new_node = self.Node(c, node)
                node.next[c] = new_node
            node = node.next[c]

        if "$" not in node.next:
            node.next["$"] = self.Node("$", node)

    def search_prefix(self, search_word):
        # fn returns up to three lexigraphically smallest words that share prefix search word
        node = self.head

        for c in search_word:
            if c not in node.next:
                return [] # no words share prefix
            node = node.next[c]
            
        end_node = node



        def dfs(node, res):
            
            if len(res) == 3:
                return
            
            if node.letter == "$":
                res.append(node)
                return

            letters = sorted([c for c in node.next])

            for letter in letters: # iterate through nodes in sorted order
                dfs(node.next[letter], res)

        res = []
        dfs(end_node, res)

        products = []
        # reverse res nodes

        # print([c.prev letter for c in res ])
        for node in res:
            suffix = deque()
            while node != end_node:
                if node.letter != "$":
                    suffix.appendleft(node.letter)
        
                node = node.prev

            suffix_str = "".join(suffix)
            products.append(search_word + suffix_str)
    
        return products



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()

        for product in products:
            trie.add_word(product)


        result = []
        for i in range(len(searchWord)):
            res = trie.search_prefix(searchWord[:i+1])

            result.append(res)
            

        return result
