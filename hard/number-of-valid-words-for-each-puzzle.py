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

    def __init__(self, wmap=None, words=[]) -> None:
        self.head = self.Node("$", "")
        self.words_added = set({})
        self.wmap = wmap

        for word in words:
            self.add_word(word)

    def add_word(self, word):

        temp = self.head
        for c in word:
            if c not in temp.children:
                new_node = self.Node(c, temp.string)
                temp.children[c] = new_node
                temp = new_node
            else:
                temp = temp.children[c]

        temp.children["$"] = True
        self.words_added.add(word)

    def words_from_node(self, puzzle_map, first_c):
        count = [0]

        def dfs(node, count):
            
            if "$" in node.children:
                if node.string.find(first_c) != -1:
                    # print(node.string)
                    count[0] += self.wmap[node.string]  

            for c in node.children:
                if c != "$":
                    if c in puzzle_map:
                        dfs(node.children[c], count)

        dfs(self.head, count)

        return count[0]

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



import re
from collections import Counter
class Solution:
    def findNumOfValidWords(self, words, puzzles):

        def to_set(word):
            s = set()
            for c in word: 
                s.add(c)

            return s
        

        def sanitize(word, d):            
            chars = set()
            s = "" 
            for c in word:
                if c not in chars:
                    chars.add(c)
                    s += c

            d[s] = 1 if s not in d else d[s] +1 
            return s


        d = {} 
        new = []        
        for w in words:
            new.append(sanitize(w, d))

        print(new)
        
        words = sorted(new)


        trie = Trie(wmap= d)
        for w in words:
            if len(w) <=7:
                trie.add_word(w)       

        arr  = [0] * len(puzzles)
        for i, p in enumerate(puzzles):
            arr[i] = trie.words_from_node(to_set(p), p[0])
        
        return arr
    
