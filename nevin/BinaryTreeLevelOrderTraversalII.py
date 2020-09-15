class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = []
        list_of_lists = []
        
        if root:
            q.append(root)
        
        while len(q) > 0:
            nodes = len(q)
            list = []
            
            while nodes > 0:
                t = q.pop(0)
                list.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                nodes -= 1
            
            list_of_lists.insert(0, list)
        
        return list_of_lists

        
# use queue to cycle through each level's nodes
#     use queue length to know when level is through
#     while enqueueing children in left to right order
# store each node value in a list
# add list to front of list of lists
