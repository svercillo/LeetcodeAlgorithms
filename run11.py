from typing import List
from collections import deque


class Solution():
    RATE_LIMIT=5 # No more than 5 cost of calls
    RATE_LIMIT_WINDOW=3 # In the past 3 seconds
    
    q1sum = 0
    q1 = deque() # less than limit
    q2 = deque() # greater than limit

    last_produced = []

    
    # `request_api_call` is called every time the caller wants to make an API call
    def request_api_call(self, cost: int) -> None:
        running = sum(self.q1)
        if running + cost <= self.RATE_LIMIT:
            self.q1.append(cost)
        else:
            self.q2.append(cost)

    # `emit_api_calls` is called by an automated system, once per second.
    # It is guaranteed to be called once per second and will always be the last (or only) call in a given second.
    # `emit_api_calls` should return a list of Costs in the same order that they are requested.
    def emit_api_calls(self) -> List[int]:        
        to_emit = []

        if len(self.last_produced) == self.RATE_LIMIT_WINDOW:
            # implement sliding window
            self.last_produced = self.last_produced[1:]

        last_produced = sum(self.last_produced)
        remaining = self.RATE_LIMIT - last_produced

        running = 0
        while len(self.q1) and self.q1[0] + running <= remaining:
            e = self.q1.popleft()
            to_emit.append(e)
            running += e

        remaining = self.RATE_LIMIT - sum(self.q1)
        running = 0
        while len(self.q2) and self.q2[0]  + running <= remaining: 
            e = self.q2.popleft()
            self.q1.append(e)
            running += e

        self.last_produced.append(sum(to_emit))

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