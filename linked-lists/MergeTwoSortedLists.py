class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
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
        
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        
        return head
