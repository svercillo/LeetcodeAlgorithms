class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        size = 0

        node = head
        while node:
            node = node.next
            size += 1


        part_size = size // k
        remainder = size % k

        important_nodes = []
        node = head
        while node:
            if remainder:
                pt_size = part_size
                remainder -= 1
            else:
                pt_size = part_size -1

            for i in range(pt_size):
                if not node:
                    return res
                node = node.next
                
                

            important_nodes.append(node)
            print(node.val)

            node = node.next

        res = [head]
        for node in important_nodes:
            if node.next:
                res.append(node.next)
            node.next = None
        
        for i in range(k - len(res)):
            res.append(None)


        return res
