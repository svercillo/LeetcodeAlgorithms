import math

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
                return f"Node: {self.string}"
                # return f"<{self.char} : {self.children.keys()}>"
            else:
                return ""

        def __repr__(self):
            return self.__str__()

    def __init__(self, words=[]) -> None:
        self.head = self.Node("$", "")
        self.words_added = set({})

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

    def words_from_node(self, node):
        words = []

        def dfs(node):
            if "$" in node.children:
                words.append(node.string)

            for c in node.children:
                if c != "$":
                    dfs(node.children[c])

        dfs(node)
        return words

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


def closestLocation(address, objects, names):

    indexes = {names[i]: i for i in range(len(names))}

    capitals = {n.lower(): n for n in names}
    names = [n.lower() for n in names]
    address = address.lower()

    def get_valid_locations(address, names):

        trie = Trie(names)
        possible_nodes = [(trie.head, 0, "")]
        finished = []

        for c in address:

            print("++++")
            print(f"Char {c}")
            next_poss = []
            while len(possible_nodes) > 0:
                poss, num_misses, curr = possible_nodes.pop()
                if num_misses > 1:
                    continue

                if poss.has(c):
                    next_poss.append((poss.children[c], num_misses, curr + c))
                elif num_misses == 0:
                    for char in poss.children:
                        if char == "$":
                            finished.append((poss, num_misses, curr))

                        elif c in poss.children[char].children:
                            next_poss.append(
                                (poss.children[char].children[c], 1, curr + char + c)
                            )

                if num_misses == 0:
                    next_poss.append((poss, 1, curr))
                    for char in poss.children:
                        if c == char:
                            continue
                        if char == "$":
                            finished.append((poss, num_misses, curr))
                        else:
                            next_poss.append((poss.children[char], 1, curr + char))

            possible_nodes = next_poss

            for poss in possible_nodes:
                print(poss)

        all_words = set()
        for poss, _, _ in possible_nodes:
            words = trie.words_from_node(poss)
            for w in words:
                all_words.add(w)

        for poss, num_misses, _ in finished:
            words = trie.words_from_node(poss)
            for w in words:
                difference = num_misses + abs(len(w) - len(address))
                if difference <= 1:
                    all_words.add(w)

        return all_words

    all_words = get_valid_locations(address, names)
    print(all_words)

    def calc_dist(row):
        if len(row) == 2:
            return (row[0] ** 2 + row[1] ** 2) ** 0.5

        vertical = False
        if row[0] == row[2]:
            vertical = True

        if not vertical:
            if row[0] <= 0 and row[2] >= 0 or row[0] >= 0 and row[1] <= 0:
                return abs(row[1])
        else:
            if row[1] <= 0 and row[3] >= 0 or row[1] >= 0 and row[3] <= 0:
                return abs(row[0])

        return min(
            (row[0] ** 2 + row[1] ** 2) ** 0.5, (row[2] ** 2 + row[3] ** 2) ** 0.5
        )

    print("valid", all_words)
    all_words = sorted([w for w in all_words])

    min_dist = math.inf
    min_word = "hubba bubba"
    for word in all_words:
        ind = indexes[capitals[word]]
        obj = objects[ind]

        dist = calc_dist(obj)
        print(dist, word)
        if dist < min_dist:
            min_dist = dist
            min_word = word

    return capitals[min_word]


res = closestLocation("Location", [[1, 1], [3, 3]], ["Locati", "Location"])

print(res)
