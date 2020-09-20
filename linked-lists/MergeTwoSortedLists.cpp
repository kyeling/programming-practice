class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL && l2 == NULL) return NULL;
        if (l1 == NULL) return l2;
        if (l2 == NULL) return l1;
        
        ListNode* head = NULL;
        if (l1->val <= l2->val){
            head = l1;
            l1 = l1->next;
        } else {
            head = l2;
            l2 = l2->next;
            head->next = l1;
        }
        ListNode* prev = head;
        ListNode* tmp = NULL;
        while (l1 != NULL && l2 != NULL){
            if (l2->val < l1->val){
                tmp = l2->next;
                l2->next = l1;
                prev->next = l2;
                l2 = tmp;
                prev = prev->next;
            } else {
                prev = l1;
                l1 = l1->next;
            }
        }
        
        if (l1 != NULL){
            prev->next = l1;
        }
        if (l2 != NULL){
            prev->next = l2;
        }
        
        return head;
    }
};
