class Solution(object):
    

    def mergeKLists(self, lists):

        interval = 1
        while interval < len(lists):
            i = 0 
            while i < len(lists)-interval:
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
                
                i += interval
            interval *= 2
            

        return lists[0] if len(lists) != 0 else None
    
    
    

    def merge_two_lists(self, l1, l2):
        print(l2)
        before_head = node = ListNode(0)
        
        while l1 and l2: 
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
                
            node = node.next
            
        if not l1:
            node.next = l2
        elif not l2: 
            node.next = l1
                
        return before_head.next
        
        
        
