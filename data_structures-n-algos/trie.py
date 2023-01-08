class Trie:
    class Node:
        def __init__(self, char, prev) -> None:
            self.char = char
            self.children = {}
            self.string = prev + char if prev != "$" else char

        def has(self, char):
            return char in self.children

        def __str__(self) -> str:
            if self.char != "$":

                return f"<{self.char} : {self.children.keys()}>"
            else:
                return ""

        def __repr__(self):
            return self.__str__()

    def __init__(self, words=[]) -> None:
        self.head = self.Node("$", "")
        self.words_added = set({})

        for word in words:
            self.add_word(word)

    def add_word(self, word) ->bool:

        temp = self.head
        for c in word:
            if c not in temp.children:
                new_node = self.Node(c, temp.string)
                temp.children[c] = new_node
                temp = new_node
            else:
                temp = temp.children[c]
        
        if "$" in temp.children:
            return True

        temp.children["$"] = True
        self.words_added.add(word)

    def has(self, word) ->bool:

        temp = self.head
        for c in word:
            if c not in temp.children:
                return False
            else:
                temp = temp.children[c]
        
        return True

    def words_from_node(self, node):
        words = []

        def dfs(node):
            if "$" in node.children:
                words.append(node.string)

            for c in node.children:
                if c != "$":
                    dfs(node.children[c])

        dfs(node)
        return words, node.num_misses

    def print_all(self):
        for word in self.words_added:
            temp = self.head
            string = ""
            for c in word:
                if c in temp.children:
                    string += f"{c}->"
                    temp = temp.children[c]
                else:
                    print(f"Character {c} not present!!!")
                    exit(1)
            if "$" in temp.children:
                print(string)
