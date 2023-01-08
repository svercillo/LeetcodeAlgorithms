class Solution:
    def addBoldTag(self, s: str, words) -> str:
        class Node:
            def __init__(self, val, child):
                self.val = val
                self.child = child

            def __str__(self):

                if self.child is not None:
                    return str(self.val) + str(self.child)
                else:
                    return str(self.val)

        def stringtoLL(string):
            if len(string) == 0:
                return None

            tail = None
            prev = None
            for i in range(len(string) - 1, -1, -1):
                this = Node(string[i], prev)
                if tail is None:
                    tail = this
                prev = this

            head = prev
            return head, tail

        intervals = []

        t = s

        for word in words:
            t = s
            addition = 0

            while word in t:
                start = t.index(word) + addition
                end = start + len(word)

                intervals.append((start, end))

                addition = end
                t = s[end:]
                print(t)
                # print(end)

            # break

        intervals.sort(key=lambda k: k[0])
        print(intervals)

        if len(intervals) == 0:
            return s

        new_ints = []

        start = intervals[0][0]
        end = intervals[0][1]

        for start2, end2 in intervals:
            if start2 > end:
                new_ints.append((start, end))
                start = start2
                end = end2

            elif end2 > end:
                end = end2

        new_ints.append((start, end))

        print(new_ints)

        head, _ = stringtoLL(s)  # head node
        node = head
        prev = None

        p = 0

        for i in range(len(new_ints)):
            start, end = new_ints[i]

            while p < start:
                prev = node
                node = node.child

                p += 1

            bhead, btail = stringtoLL("<b>")

            if prev is None:
                head = bhead
            else:
                prev.child = bhead

            btail.child = node

            while p < end and node is not None:
                prev = node
                node = node.child
                p += 1

            bhead, btail = stringtoLL("</b>")
            prev.child = bhead
            btail.child = node

        return str(head)


res = Solution().addBoldTag("abcdef", ["a", "c", "e", "g"])
# res = Solution().addBoldTag("aaabbcc", ["a", "b", "c"])
# res = Solution().addBoldTag("abcdef", ["a", "c", "e", "g"])
print(res)
