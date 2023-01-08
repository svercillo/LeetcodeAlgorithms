class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    
        dp = deque()
        for ast in asteroids:
            if ast >= 0: 
                dp.append(ast)
            else:
                
                while len(dp) > 0 and -ast > dp[-1] and dp[-1] > 0:
                    dp.pop()
                
                if len(dp) > 0 and dp[-1] > 0:
                    if dp[-1] == -ast:
                        dp.pop()
                else:
                    dp.append(ast)
        return [a for a in dp]
