class LinkedList:
    class Iterator:
        def __init__(self, linkedlist) -> None:
            self.cur = linkedlist.head
            self.linkedlist = linkedlist

        def __iter__(self):
            return self

        def __next__(self):
            if self.cur is None:
                raise StopIteration
            res = self.cur

            self.cur = self.cur.next
            return res

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

        def __str__(self) -> str:
            return f"{self.data}->"

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data) -> Node:
        if isinstance(data, self.Node):
            node = data
        else:
            node = self.Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1
        return node

    def remove(self, node: Node):
        if self.head is None:
            return -1  # element doesnt exist

        if id(self.head) == id(self.tail):  # pop off first element, len == 1
            self.head = None
            self.tail = None
        elif node == self.head:  # pop off first element, len > 1
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
        elif node == self.tail:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

        self.size -= 1

        node.prev = None
        node.next = None

        return node

    def pop_tail(self) -> Node:
        return self.remove(self.tail)

    def pop_head(self) -> Node:
        return self.remove(self.head)

    def is_empty(self) -> bool:
        return self.size == 0

    def __repr__(self) -> str:
        temp = self.head
        s = ""
        while temp is not None:
            s += str(temp)
            temp = temp.next
        return s

    def __str__(self) -> str:
        return self.__repr__()

    def __iter__(self):
        return self.Iterator(self)


class Solution:
    def sortString(self, s: str) -> str:

        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0

            freq[c] += 1

        ll = LinkedList()

        arr = [c for c in freq]
        arr.sort()

        for c in arr:
            ll.append([c, freq[c]])

        res = ""

        while ll.head:
            to_remove = []
            for node in ll:
                res += node.data[0]
                node.data[1] -= 1
                if node.data[1] == 0:
                    to_remove.append(node)

            for node in to_remove:
                ll.remove(node)


            to_remove = []
            node = ll.tail

            while node:
                res += node.data[0]
                node.data[1] -= 1
                if node.data[1] == 0:
                    to_remove.append(node)

                node = node.prev

            for node in to_remove:
                ll.remove(node)

        return res
