class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

        def __str__(self) -> str:
            return f"{self.val}->"

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):

        node = self.Node(data)

        if not self.head:
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        return node

    def remove_all_after_inc(self, node):
        if not node:
            return

        if node == self.head:
            self.head = None
            self.tail = None
        else:
            prev = node.prev
            nxt = node.next

            prev.next = nxt
            if nxt:
                nxt.prev = prev

            self.tail = prev

        node.prev = None
        node.next = None

    def print(self):
        temp = self.head
        s = ""
        while temp is not None:
            s += str(temp)
            temp = temp.next

        print(s)
        return s


class BrowserHistory:
    def __init__(self, homepage: str):
        self.ll = LinkedList()
        self.ll.append(homepage)
        self.current = self.ll.tail


    def visit(self, url: str) -> None:
        print("printing ...")
        
        self.ll.remove_all_after_inc(self.current.next)
        self.ll.append(url)
        self.ll.print()
        self.current = self.ll.tail

    def back(self, steps: int) -> str:
        node = self.current

        while node.prev and steps > 0:
            steps -= 1
            node = node.prev

        self.current = node
        return node.val

    def forward(self, steps: int) -> str:

        node = self.current

        while node.next and steps > 0:
            steps -= 1
            node = node.next

        self.current = node
        return node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
