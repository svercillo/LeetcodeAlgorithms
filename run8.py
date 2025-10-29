from typing import List
from collections import deque


class Solution():
    RATE_LIMIT=4
    
    q1 = deque()
    sq1 = 0 # total sum of q1
    q2 = deque()
    
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
        res = [e for e in self.q1]
        self.q1 = deque()
        q3 = deque()
    
        running = 0 
        for _, cost in enumerate(self.q2):
            if running + cost <= self.RATE_LIMIT: 
                self.q1.append(cost)
                running += cost
            else:
                q3.append(cost)

        self.q2 = q3
        self.sq1 = running

        return res
        


solution = Solution()
def request_api_call(v):
    res = solution.request_api_call(v)
    # print(res)

def emit_api_calls():
    res = solution.emit_api_calls()
    print(res)
    


emit_api_calls()
# The request_api_call() function can be invoked multiple (from zero to infinite) times within a single second.
# Calls to emit_api_calls() are made once every second, and will be the last (or only) call each second.
request_api_call(7) # An API call with a cost of 2 is requested.
# request_api_call(-1) # An API call with a cost of 2 is requested.
request_api_call(0) # An API call with a cost of 2 is requested.
request_api_call(1) # Another API call with a cost of 2 is requested, thus we have [2, 2].
request_api_call(1) # Continuing, we now have API calls with costs [2, 2, 1].
request_api_call(1) # [2, 2, 1, 1].
emit_api_calls() # Returns [2, 2]. Only the first two API calls are processed due to the rate limit of 4.
request_api_call(3) # In the next second, a call costing 3 is requested, so we have [1, 1, 3].
request_api_call(1) # In the next second, a call costing 3 is requested, so we have [1, 1, 3].
emit_api_calls() # Returns [1, 1]. Requests from earlier are processed; the recent request is not, as it would exceed the rate limit.

# If a time passes without any new request_api_calls, any pending API calls are processed in subsequent seconds.
emit_api_calls() # Returns [3].