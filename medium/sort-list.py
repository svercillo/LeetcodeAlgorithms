# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def merge(left, right):
 
    res_head = ListNode(-1)
    res = res_head
    while left and right:
        if left.val < right.val: 
            nxt = ListNode(left.val)
            left = left.next
        else:
            nxt = ListNode(right.val)
            right = right.next
            
        res.next = nxt
        res = res.next
    while left:
        res.next = ListNode(left.val)
        res = res.next
        left = left.next
        
    while right:
        res.next = ListNode(right.val)
        res = res.next
        right = right.next
        
    return res_head.next

def mergesort(head):
    if not head:
        return None
    if not head.next:
        return head
    
    size = 0
    node = head
    while node != None:
        node = node.next
        size += 1
        
    
    node = head
    size //= 2 
    while size:
        last_node = node
        node = node.next
    
        size -=1
    
    left = head
    right = node
    
    last_node.next = None

    left_res = mergesort(left)
    right_res = mergesort(right)
    
    return merge(left_res, right_res)
    

    
class Solution:
    def sortList(self, head):
        return mergesort(head)
                
