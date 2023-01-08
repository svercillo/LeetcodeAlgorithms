class Solution:
    def findingUsersActiveMinutes(self, logs, k: int):
        _map = {}
        for user, time in logs:
            if user not in _map:
                _map[user] = set()
                
            _map[user].add(time)
        

        print(_map)
        res = [0] * k
        
        for key in _map: 
            if len(_map[key]) <= k:
                res[len(_map[key])-1] += 1
                
                
        return res
            
