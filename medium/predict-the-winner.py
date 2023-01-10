class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def canA_win(lp, rp, move_A, player1, player2):
            n = len(nums)
        
            if lp == rp:
                if move_A: 
                    player1 += nums[lp]
                else:
                    player2 += nums[lp]

                print(player1, player2)
                return player1 >= player2
            
            if move_A:
                if (
                    canA_win(lp+1, rp, not move_A, player1+nums[lp], player2)
                    or canA_win(lp, rp-1, not move_A, player1+nums[rp], player2)
                ):
                    return True
                else:
                    return False
            else:
                if (
                    canA_win(lp+1, rp, not move_A, player1, player2 + nums[lp])
                    and canA_win(lp, rp-1, not move_A, player1, player2 + nums[rp])
                ):
                    return True

                else:
                    return False

        return canA_win(0,n-1, True, 0, 0)
