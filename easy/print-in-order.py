from threading import Thread, Lock

class Foo:
    mutex = Lock()
    def __init__(self):
        self.val = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:

        value_needed = 1
        while True:
            self.mutex.acquire()
            if value_needed == self.val:
                break 
            self.mutex.release()
        
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.val +=1
        self.mutex.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        value_needed = 2
        while True:
            self.mutex.acquire()
            if value_needed == self.val:
                break 
            self.mutex.release()
        
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.val +=1
        self.mutex.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        value_needed = 3
        while True:
            self.mutex.acquire()
            if value_needed == self.val:
                break 
            self.mutex.release()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.val +=1
        self.mutex.release()
