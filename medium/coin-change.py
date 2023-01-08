class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        q = [amount]
        
        visited = set()
        
        num_coins = 0
        while len(q) > 0:
            newq = []
            
            for value in q:    
                if value in visited:
                    continue
                
                visited.add(value)
                if value == 0:
                    return num_coins
                
                for coin in coins:
                    remaining = value - coin
                    if remaining >=0: 
                        newq.append(remaining)
                
            
            q = newq
            num_coins += 1
            
        
        return -1
