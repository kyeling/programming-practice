// Slow and fast pointers approach: time O(n), space O(1)

bool hasCycle(struct ListNode *head) {
    if(head == NULL) return false;
    struct ListNode* fast = head;
    struct ListNode* slow = head;
    while(fast->next != NULL && fast->next->next != NULL){
        fast = fast->next->next;
        slow = slow->next;
        if(fast == slow) return true;
    }
    return false;
}
