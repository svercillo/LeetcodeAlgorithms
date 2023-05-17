class Trie:

    class Node:
        def __init__(self, letter):
            self.letter = letter
            self.next = {}
            self.words_ending_here = 0


    def __init__(self):
        self.head = self.Node("%")

    def insert(self, word: str) -> None:
        node = self.head

        for c in word:
            if c not in node.next:
                node.next[c] = self.Node(c)
            node = node.next[c]
        node.words_ending_here += 1
        
    def countWordsEqualTo(self, word: str) -> int:

        node = self.head
        for c in word:
            if c not in node.next:
                return 0

            node = node.next[c]

        return node.words_ending_here

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.head

        for c in prefix:
            if c not in node.next:
                return 0
            node = node.next[c]
            

        def count_num_words(node):
            total = node.words_ending_here
            for c in node.next:
                total += count_num_words(node.next[c])

            return total

        return count_num_words(node)

    def erase(self, word: str) -> None:
        node = self.head
        for c in word:
            node = node.next[c]
        
        node.words_ending_here -= 1
        
