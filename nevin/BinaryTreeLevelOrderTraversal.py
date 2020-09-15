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
