# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# merge one list at a time
# time O(kn) where k = number of lists, n = max elements in list
# space O(1) bc modify in place
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        for i in range(1, len(lists)):
            lists[0] = self.mergeTwoLists(lists[0], lists[i])
        return lists[0]
            
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:    
        if not l1 and not l2: return None
        elif not l1: return l2
        elif not l2: return l1
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            head.next = l1
        prev = head
            
        while l1 and l2:
            if l2.val < l1.val:
                tmp = l2.next
                l2.next = l1
                prev.next = l2
                l2 = tmp
                prev = prev.next
            else:
                prev = l1
                l1 = l1.next
        
        if l1: prev.next = l1
        if l2: prev.next = l2
        
        return head
    
    
# better approach: divide and conque merge (merge in pairs, then merge in pairs again, etc)
# time O(n logk) where k = is number of lists, n = max number of elements in list
# space O(1) bc merge in place
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0: return None
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]
    
    # uses same mergeTwoLists() function as earlier
