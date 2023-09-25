class Solution:
    def canIWin(self, max_choosable: int, desired_total: int) -> bool:


        if desired_total == 0:
            return True

        @cache
        def canForceWin(bitmask, score, myTurn): 
            nonlocal max_choosable, desired_total
            
            if score >= desired_total:
                return not myTurn

            win_exists = False
            all_wins = True
            used_any = False
            for i in range(1, max_choosable+1):
                if bitmask & 2 ** i == 0:
                    used_any = True
                    res = canForceWin(bitmask + 2 ** i, score + i, not myTurn)
                    if not res:
                        all_wins = False
                    if res:
                        win_exists = True
x
                if not myTurn and all_wins == False or myTurn and win_exists:
                    break 
            
            if not myTurn:
                return all_wins and used_any
            else:
                return win_exists


        return canForceWin(0, 0, True)

        
        
            
            

