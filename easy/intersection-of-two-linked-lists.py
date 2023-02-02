/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode*> nodesA; 


        while (headA != NULL){
            nodesA.insert(headA);
            headA = headA->next;
        }

        while (headB != NULL){
            if (nodesA.find(headB) != nodesA.end()){
                return headB;
            }
            headB = headB->next;

        }
        return NULL;
   
    }
};
