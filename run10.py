from typing import List
from collections import deque


class Solution():
    RATE_LIMIT=5 # No more than 5 cost of calls
    RATE_LIMIT_WINDOW=3 # In the past 3 seconds
    
    q1 = deque()
    sq1 = 0 # total sum of q1
    q2 = deque()

    emitted = deque()
    emiitted_sum = 0

    def __init__(self):
        for _ in range(self.RATE_LIMIT_WINDOW):
            self.emitted.append(0)
    
    # `request_api_call` is called every time the caller wants to make an API call
    def request_api_call(self, cost: int) -> None:
        if cost < 0 or cost > self.RATE_LIMIT: 
            raise Exception("Invalid cost", cost)
        elif cost == 0:
            return

        if self.sq1 + cost <= self.RATE_LIMIT:
            self.q1.append(cost)
            self.sq1 += cost
        else:
            self.q2.append(cost)
        

    # `emit_api_calls` is called by an automated system, once per second.
    # It is guaranteed to be called once per second and will always be the last (or only) call in a given second.
    # `emit_api_calls` should return a list of Costs in the same order that they are requested.
    def emit_api_calls(self) -> List[int]:
        # calc sum of emitted window MINUS 1 second
        if len(self.emitted):
            top = self.emitted.popleft()
            self.emiitted_sum -= top

        semitted = 0
        to_emit = []
        remaining_space = self.RATE_LIMIT - self.emiitted_sum

        # emit everything we can from things less than the rate limit
        running = self.sq1
        while len(self.q1) and self.q1[0] <= remaining_space:
            e = self.q1.popleft()

            remaining_space -= e
            to_emit.append(e)
            semitted += e
            running -= e 

        # rebalance q1, q2 if possible
        while len(self.q2) and self.q2[0] + running <= self.RATE_LIMIT:
            e = self.q2.popleft()
            self.q1.append(e)
            running += e
        
        self.sq1 = running
        self.emitted.append(semitted)
        self.emiitted_sum += semitted


        return to_emit

        
    

        




        


solution = Solution()
def request_api_call(v):
    res = solution.request_api_call(v)
    # print(res)

def emit_api_calls():
    res = solution.emit_api_calls()
    print(res)
    



request_api_call(2) 
emit_api_calls() # -> [2]
request_api_call(3)
request_api_call(4) 
request_api_call(5) 
emit_api_calls() # -> [3]. Emitting 3 is ok because 2+3 <= 5.
emit_api_calls() # -> []. We have emitted 5 cost of calls last three seconds, so can't fit a 4 cost call
emit_api_calls() # -> []. We have emitted 3 cost of calls in the last three seconds, so still can't fit a 4 cost call
emit_api_calls() # -> [4]. 3-cost call from time 1 is no longer in the rate limit window, so can afford the 4-cost call
emit_api_calls() # -> [] 
emit_api_calls() # -> [] 
emit_api_calls() # -> [5]