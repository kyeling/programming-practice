# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None, k=2
#          b4        s         f
# tmp = 2.next = 3
# 2.next = 4.next
# 4.next = tmp
# tmp = 2
# 1.next = 4
# 3.next = 2

# [7, 9, 6, 6, 7, 8, 3, 0, 9, 5], k=5
#           b4 s              f
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)
        b4_front = dummy
        for i in range(k-1):
            b4_front = b4_front.next
            
        slowptr, fastptr = dummy, b4_front.next
        while fastptr.next is not None:
            slowptr = slowptr.next
            fastptr = fastptr.next
        
        # front = b4_front.next
        # back = slowptr.next
        # tmp = front.next
        # front.next = back.next
        # back.next = tmp
        # b4_front.next = back
        # slowptr.next = front
        if slowptr.next == b4_front:
            tmp = b4_front
            b4_front = slowptr
            slowptr = tmp
            
        if b4_front.next == slowptr:
            front = b4_front.next
            back = slowptr.next
            front.next = back.next # back.next
            b4_front.next = back # back
            back.next = front

        elif b4_front is not slowptr:
            tmp = b4_front.next.next # temporarily store front.next node
            b4_front.next.next = slowptr.next.next # front.next = back.next
            slowptr.next.next = tmp # back.next = front.next
            tmp = b4_front.next
            b4_front.next = slowptr.next # bfront.next = bback.next
            slowptr.next = tmp  # bback.next = bfront.next
        
        return dummy.next
        
# get pointers to the kth nodes from the front and back
# front node: iterate down list that many times
# back node: fast pointer k nodes ahead, once fast ptr hits end, slow ptr is at k from end
# need node before front node
#   set before.next -> back
#   set back.next -> front.next
# tmp to save node

# edge case: k = 1: swap first and last, no before pointer or dummy pointer
# dummy.next -> head
# dummy -> 1 -> 2 -> 3 -> 4 -> 5
# before_front ptr: iterate k-1 times 
# before_back ptr: fastptr = before_front 
#                  slowptr = dummy
# 
# edge case is if nodes to swap are same node
# 
