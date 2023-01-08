class Solution:
    def isOneEditDistance(self, s_str: str, t_str: str) -> bool:

        if s_str == "" and len(t_str) == 1 or t_str == "" and len(s_str) == 1:
            return True

        s = []
        for c in s_str:
            s.append(c)

        t = []
        for c in t_str:
            t.append(c)

        def compare_strings(s, t, sp, tp, edit_availible):

            while sp < len(s) and tp < len(t):

                if s[sp] != t[tp]:
                    if not edit_availible:
                        return False

                    new_s = s.copy()
                    new_t = t.copy()

                    condition = False

                    # skip character
                    condition = condition or compare_strings(
                        new_s, new_t, sp + 1, tp, False
                    )
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp + 1, False
                    )

                    # change character
                    new_s[sp] = new_t[tp]
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp, False
                    )

                    new_s[sp] = s[sp]
                    new_t[tp] = new_s[sp]
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp, False
                    )

                    # insert character
                    new_t[tp] = t[tp]
                    new_t = new_t[:tp] + [new_s[sp]] + new_t[tp:]
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp, False
                    )

                    new_t = new_t[:tp] + new_t[tp + 1 :]
                    new_s = new_s[:sp] + [new_t[tp]] + new_s[sp:]
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp, False
                    )

                    if condition:
                        return True

                sp += 1
                tp += 1

            if edit_availible:
                if len(s) != len(t):

                    if len(s) > len(t):
                        temp = s
                        s = t
                        t = temp

                    new_s = s.copy()
                    new_t = t.copy()

                    # insert character
                    new_s = new_s + [new_t[tp]]

                    condition = False
                    condition = condition or compare_strings(
                        new_s, new_t, sp, tp, False
                    )

                    if condition:
                        return True

                return True
            else:
                return False

        return compare_strings(s, t, 0, 0, True)


res = Solution().isOneEditDistance("", "")

print(res)
