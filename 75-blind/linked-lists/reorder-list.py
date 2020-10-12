/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void reorderList(struct ListNode* head){
    if(head == NULL || head->next == NULL || head->next->next == NULL) return;
    
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while(fast->next != NULL){
        slow = slow->next;
        fast = fast->next;
        if(fast->next != NULL){
            fast = fast->next;
        }
    }
    
    // reverse list from leetcode problem 206
    struct ListNode* curr;
    struct ListNode* rev = NULL;
    while(slow != NULL){
        curr = slow;
        slow = slow->next;
        curr->next = rev;
        rev = curr;
    }
    slow = rev;
    
    struct ListNode* tmp = NULL;
    curr = head;
    while(curr->next != NULL && slow->next != NULL){
        tmp = slow->next;
        slow->next = curr->next;
        curr->next = slow;
        curr = curr->next->next;
        slow = tmp;
    }
}
