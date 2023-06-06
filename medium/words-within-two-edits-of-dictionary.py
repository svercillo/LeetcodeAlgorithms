class Trie:
    class Node:
        def __init__(self, char):
            self.char = char
            self.children = {}

    def __init__(self):
        self.head = self.Node("$")

    def add_word(self, word):
        node = self.head
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = self.Node(c)
                node.children[c] = new_node
                node = new_node
        
        node.children["$"] = True


    @cache
    def contains(self, node, word, ind):
        # print(node.char, word, ind)
        while ind < len(word):
            c = word[ind]
            
            if c == "*":
                for new_char in node.children:
                    if self.contains(node.children[new_char], word, ind + 1):
                        return True
            elif c in node.children: 
                node = node.children[c]
            else:
                return False

            ind += 1
            
        return "$" in node.children
            

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)
        

        
        res = []
        for word in queries:

            contains_word = False
            if len(word) == 1:
                if trie.contains(trie.head, "*", 0):
                    contains_word = True
            for i in range(len(word)):
                for j in range(i+1, len(word)):
                    carr = [c for c in word]
                    carr[i] = "*"
                    carr[j] = "*"

                    if trie.contains(trie.head, "".join(carr), 0):
                        contains_word = True
                        break
                if contains_word:
                    break
            if contains_word:
                res.append(word)

        return res
                        
