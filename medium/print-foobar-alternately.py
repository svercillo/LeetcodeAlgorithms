from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.mutex = Lock()
        self.bool = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            
            while True:
                self.mutex.acquire()
                if self.bool ==True:
                    break 
                self.mutex.release()
                
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bool = False
            self.mutex.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            while True:
                self.mutex.acquire()
                if self.bool == False:
                    break
                self.mutex.release()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bool = True
            self.mutex.release()
