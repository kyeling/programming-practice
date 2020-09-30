// iterative solution: time O(n), space O(1)

struct ListNode* reverseList(struct ListNode* head){
    if(head == NULL || head->next == NULL) return head;
    struct ListNode* curr;
    struct ListNode* revHead = NULL;
    while(head != NULL){
        curr = head;
        head = head->next;
        curr->next = revHead;
        revHead = curr;
    }
    return revHead;
}


// recursive solution: time and space O(n)

struct ListNode* reverseList(struct ListNode* head){
    if(head == NULL || head->next == NULL) return head;
    struct ListNode* curr = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return curr;
}
