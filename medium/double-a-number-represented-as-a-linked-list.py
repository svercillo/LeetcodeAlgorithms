# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head

        string = []
        while temp:
            string.append(temp.val)
            temp = temp.next



        rev_string = string[::-1]
        prehead = ListNode()
        node = prehead
        carry_over = False
        for val in rev_string:
            new_val = val * 2 

            if carry_over:
                new_val += 1

            if new_val >= 10:
                carry_over = True

            else:
                carry_over = False

            new_node = ListNode(int(str(new_val)[-1]))
            node.next = new_node
            node = new_node

        if carry_over:
            new_node = ListNode(1)
            node.next = new_node

        

        def reverse_ll(head):
            node = head
            last_node = None
            while node:
                nxt_node = node.next
                node.next = last_node
                last_node = node
            
                node = nxt_node
            
            return last_node
    
        return reverse_ll(prehead.next)


