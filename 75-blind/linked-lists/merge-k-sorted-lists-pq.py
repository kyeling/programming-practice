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
