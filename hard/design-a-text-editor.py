from collections import deque

class TextEditor:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)
        
    def deleteText(self, k: int) -> int:
        chars_deleted = 0 
        while chars_deleted < k and len(self.left) > 0:
            self.left.pop()
            chars_deleted += 1
            
        return chars_deleted

    def cursorLeft(self, k: int) -> str:
        chars_moved = 0
        while len(self.left) > 0 and chars_moved < k:
            self.right.appendleft(self.left.pop())
            chars_moved += 1

        return self.last_buffer()

    def cursorRight(self, k: int) -> str:
        chars_moved = 0
        while len(self.right) > 0 and chars_moved < k:
            self.left.append(self.right.popleft())
            chars_moved += 1

        return self.last_buffer()
        
    
    def last_buffer(self):
        backfill = deque()
        chars_moved = 0 
        while len(self.left) and chars_moved < 10:
            backfill.appendleft(self.left.pop())
            chars_moved += 1
        
        res = ""
        for c in backfill:
            self.left.append(c)
            res += c

        return res
        
    

    def print_state(self): 
        res = ""
        for c in self.left:
            res += c
        res += "|"
        
        for c in self.right:
            res += c

        return res
    
