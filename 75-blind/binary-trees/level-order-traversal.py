class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = []
        level = []
        levels = []
        
        if not root:
            return levels
        q.append(root)
        
        while len(q) > 0:
            num = len(q)
            while num > 0:
                t = q.pop(0)
                level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                num -= 1
            
            levels.append(level.copy())
            level.clear()
        
        return levels
    
    
# Jaden's solution
# can also use stack and pop
# time O(V+E) or O(2n) if recursive, but O(n) otherwise, where n is number of nodes
# space O(V+E) 
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        nodes = []
        
        # initialize queue
        nodeDeque = deque([root])
        
        #bfs until queue empty
        while nodeDeque:
            levellen = len(nodeDeque)
            levelnodes = []
            for i in range(levellen):
                curNode = nodeDeque.popleft()
                levelnodes.append(curNode.val)
                
                if curNode.left:
                    nodeDeque.append(curNode.left)
                if curNode.right:
                    nodeDeque.append(curNode.right)
                    
            nodes.append(levelnodes)
        return nodes
