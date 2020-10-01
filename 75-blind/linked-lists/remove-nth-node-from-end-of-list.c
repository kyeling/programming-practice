/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// one pass approach: time O(n), space O(1)
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    if(head == NULL) return head;
    struct ListNode* fastPtr = head;
    struct ListNode* slowPtr = head;
    
    for(int i = 0; i < n; i++){
        fastPtr = fastPtr->next;
    }
    
    if(fastPtr == NULL){
        head = head->next;
        return head;
    }
    
    while(fastPtr->next != NULL){
        slowPtr = slowPtr->next;
        fastPtr = fastPtr->next;
    }
    slowPtr->next = slowPtr->next->next;
    return head;
}
