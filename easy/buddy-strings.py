class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        n, m = len(s), len(goal)
        if n != m:
            return False
        

        differences = []
        for i in range(n):
            if s[i] != goal[i]:
                differences.append(i)
                if len(differences) > 2:
                    return False

        can_swap_the_same = False
        freq = {}
        for c in goal:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            if freq[c] >= 2:
                can_swap_the_same = True
                break


        if len(differences) == 0 and can_swap_the_same:
            return True
        elif len(differences) == 2:
            first_s = s[differences[0]]
            second_s = s[differences[1]]

            first_g = goal[differences[0]]
            second_g = goal[differences[1]]

            print()

            if first_s == second_g and second_s == first_g:
                return True

            return False
