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
    
    
# divide and conque merge (merge in pairs, then merge in pairs again, etc)
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
    
    
    
# PQ approach
# time O(n logk) bc inserting into PQ is logn and eventually insert all n nodes
# space O(n + k) bc new linked list is O(n) and PQ stores at max the length of one list at a time
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)  # dummy node to point to new linked list
        q = PriorityQueue()
        
        # initial iteration through lists, if linked list not empty, put its head as a (value, node) pair in PQ
        for l in lists:
            if l: q.put((l.val, l)) 
        
        # get the (value, node) pair at the front of the PQ and add a new node with the value to the linked list
        # use node.next to get the next lowest element of the linked list to add to the PQ
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node: q.put((node.val, node)) 
        return head.next
