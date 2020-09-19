class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = 0
        exp = 0
    
        while l1 and l2:
            total += (l1.val + l2.val) * (10 ** exp)
            exp += 1
            l1 = l1.next
            l2 = l2.next

        while l1:
            total += l1.val * (10 ** exp)
            exp += 1
            l1 = l1.next

        while l2:
            total += l2.val * (10 ** exp)
            exp += 1
            l2 = l2.next

        total_str = str(total)[::-1]
        result = ListNode()
        curr = result
        
        for c in total_str:
            curr.next = ListNode()
            curr = curr.next
            curr.val = int(c)
            
        return result.next
        
# check that next value exists for both lists
# add l1.val and l2.val multiplied by exp (0, 1, 2, etc)
# increment exp
