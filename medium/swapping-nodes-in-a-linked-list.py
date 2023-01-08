class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
    
        size = 0
        
        node = head
        while node:
            size +=1
            node = node.next
            
        if size == 1: 
            return head
            
        b_1 = None
        c_1 = None
        
        b_2 = None
        c_2 = None
        
        k = min(k, size- k +1)
    
        prev = None
        node = head
        index = 1
        
        while index <= size:

            
            if index == k:
                b_1 = prev
                c_1 = node
                
            elif index == size - k +1:
                b_2 = prev
                c_2 = node
            
            prev = node
            node = node.next
            
            index +=  1
        
        try:
        
            a_1 = c_1.next
            a_2 = c_2.next

            if b_2 == c_1:

                if b_1 :                 
                    b_1.next = c_2
                else: 
                    head = c_2
                c_1.next = a_2
                c_2.next = c_1


            else:

                if b_1:
                    b_1.next = c_2 
                else: 
                    head = c_2


                c_2.next = a_1


                b_2.next = c_1
                c_1.next = a_2
            
        except Exception as err:
            print(err)
        


        
        
        return head
