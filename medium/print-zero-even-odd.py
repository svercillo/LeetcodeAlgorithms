from threading import Lock, Semaphore
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = 7
        self.mutex = Lock()
        self.z = Semaphore()
        self.e = Semaphore(0)
        self.o = Semaphore(0)
        self.val = 1;
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        while True:
            # print("enter")
            self.z.acquire()
            
            # print("v", self.val)
            with self.mutex:
                if self.val == self.n+1:
                    self.e.release()
                    self.o.release()
                    return;
            
            print("0")
            if self.val %2==0:
                self.e.release()
            else: 
                self.o.release()
            
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:

        while True:
            self.e.acquire()
            with self.mutex:
                if self.val == self.n+1:
                    self.z.release()
                    return;
            

            print(self.val)
            self.val += 1
            # self.val = self.n
            # print("releasing")
            self.z.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        # print("odd")
        while True:
            self.o.acquire()
            with self.mutex:
                if self.val == self.n+1:
                    self.z.release()
                    return;
            

            print(self.val)
            self.val += 1
            # self.val = self.n
            # print("releasing")
            self.z.release()
            
