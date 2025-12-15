from pprint import pprint

class Node:
    def __init__(self, val, time, freq):
        self.val = val
        self.time = time 
        self.freq = freq
        self.invalid = False
    
    def __repr__(self):
        return "Node<" + str(self.val) + " f: "+ str(self.freq) + " t: " + str(self.time)

    def __lt__(self, other):
        if self.freq == other.freq: 
            return self.time > other.time
        return self.freq > other.freq

class FreqStack:
    def __init__(self):
        self.vstacks = defaultdict(list)
        self.q = []
        self.clock = 0

    def push(self, val: int) -> None:
        q = self.q 
        vstacks = self.vstacks

        f =1 
        if len(vstacks[val]):
            top = vstacks[val][-1]
            top.invalid = True
            f = top.freq + 1

        nxtnode = Node(val, self.clock, f)
        vstacks[val].append(nxtnode)
        heappush(q, nxtnode)

        self.clock += 1


    def pop(self) -> int:
        q = self.q
        vstacks = self.vstacks


        while q[0].invalid:
            heappop(q)

        top = heappop(q)
        vstacks[top.val].pop()

        if len(vstacks[top.val]):
            vstacks[top.val][-1].invalid = False
        

        return top.val





# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
