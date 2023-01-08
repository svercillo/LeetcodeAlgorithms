# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ll1 = l1
        ll2 = l2
        if not l1: return l2
        if not l2: return l1
        
        str1 = ""
        str2 = ""
        while ll1:
            str1 += str(ll1.val)
            ll1=ll1.next
        while ll2:
            str2 += str(ll2.val)
            ll2=ll2.next
        
        s = int(str1[::-1]) + int(str2[::-1])
        s = str(s)[::-1]
        last = ListNode(int(s[0]))
        head = last
        for i in range(1, len(s)):

            new = ListNode(int(s[i]))
            last.next = new
            last = new
        return head
        
