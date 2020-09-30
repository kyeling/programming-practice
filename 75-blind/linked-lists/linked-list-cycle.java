// Hashtable approach: time O(n), space O(n)

public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null) return false;
        HashSet<ListNode> visited = new HashSet<>();
        while(head.next != null){
            if(visited.contains(head)){
                return true;
            }
            visited.add(head);
            head = head.next;
        }
        return false;
    }
}
