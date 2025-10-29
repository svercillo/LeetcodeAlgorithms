class Node:
    def __init__(self, value):
        self.children = {}
        self.value = value

class WordDictionary:

    def __init__(self):
        self.head = Node("+")
    
    def addWord(self, word: str) -> None:
        node = self.head 

        for c in word:
            if c in node.children:
                node = node.children[c]
            else: 
                newnode = Node(c)
                node.children[c] = newnode
                node = newnode
        
        node.children["*"] = Node("*")

    def search(self, word: str) -> bool:
        def contains(node, word, ind):
            if ind == len(word):
                return "*" in node.children
            
            chars = []
            if word[ind] == ".":
                for c in node.children: 
                    chars.append(c) 
            else:
                if word[ind] not in node.children:

                    print(word[ind])
                    return False
                chars =[word[ind]]
        
            for c in chars:
                new_node = node.children[c]
                if contains(new_node, word, ind + 1):
                    return True

            return False
                    
        return contains(self.head, word, 0)



        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
