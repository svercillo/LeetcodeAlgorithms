# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        
        top = head
        
        size = 0
        while top:
            
            size +=1
            top = top.next
            
        
        num_jumps_to_half = size //2
        if size % 2 != 0:
            num_jumps_to_half += 1 
        
        
        half = head
        while num_jumps_to_half:
            half = half.next
            
            num_jumps_to_half -= 1
            
            
        top = head
        end = self.reverseList(half)
        
        
        while end:
            if head.val != end.val:
                return False
            
            
            head = head.next
            end = end.next
            
        return True
            
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr = head
        
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev
        
        


            
        
        
        
        
