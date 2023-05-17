class Trie:

    class Node:
        def __init__(self, string, val):
            self.string = string
            self.val = val
            self.next = {}

    def __init__(self):
        self.head = self.Node("$", 1)
    
    def add_word(self, strs_arr, val) ->bool:
        
        node = self.head
        for string in strs_arr[:-1]:

            if string not in node.next:
                return False

            node = node.next[string]

        if strs_arr[-1] in node.next:
            return False
        node.next[strs_arr[-1]] = self.Node(strs_arr[-1], val)

        return True

    def get_word(self, strs_arr):
        node = self.head
    
        for string in strs_arr:
            if string not in node.next:
                return -1

            node = node.next[string]

        return node.val


class FileSystem:

    def __init__(self):
        self.trie = Trie()
        

    def tokenize_path(self, path):
        return path.split("/")[1:]


    def createPath(self, path: str, value: int) -> bool:

        tkns = self.tokenize_path(path)
        print(tkns)
        return self.trie.add_word(tkns, value)
        

    def get(self, path: str) -> int:
        tkns = self.tokenize_path(path)
        return self.trie.get_word(tkns)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
