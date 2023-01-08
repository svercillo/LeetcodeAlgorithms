class LL:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, string=None):
        self.head = None
        self.tail = None
        self.size = 0

        if string:
            for c in string:
                self.append(c)

    def append(self, val) -> Node:

        node = self.Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return node

    def remove(self, node):
        if not node or not self.head or not self.tail:
            return -1

        if id(self.head) == id(self.tail):
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = self.head.next

        elif node == self.tail:
            second_last = self.tail.prev
            second_last.next = None
            self.tail = second_last
        else:
            prev = node.prev
            _next = node.next
            prev.next = _next
            _next.prev = prev

        node.prev = None
        node.next = None
        return node

    def pop(self):
        return self.remove(self.tail)

    def pop_head(self):
        return self.remove(self.head)

    def __str__(self):
        node = self.head
        res = ""
        while node:
            res += str(node.val)
            node = node.next
        return res


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)

        if n < 11:
            return []

        current = s[:10]

        llist = LL(current)

        res = set()
        dna = {current: 9}  # end ind of string

        l, r = 0, 9
        while r < n - 1:

            l += 1
            r += 1

            llist.pop_head()
            llist.append(s[r])

            string = str(llist)
            # print(string, dna)
            if string in dna:
                res.add(string)
            else:
                dna[string] = r

        return list(res)
