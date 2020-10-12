class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.helper([],0,root)
    
    # res (short for result) is the list of lists
    # the level tells us what index of res we're appending to since we pass level+1 to recursive calls on the children
    # finally we need a node to call the function on and append to one of the lists in res based on the current level
    def helper(self,res,level,node) -> List[List[int]]:
        if not node: return None
        
        # before calling this function on the children, check to make sure there's a list in res to represent the next level
        if len(res) < level+1:
            res.append([])
        res[level].append(node.val)
        
        self.helper(res,level+1,node.left)  # call helper to insert the left child into res and then call helper on its own children
        self.helper(res,level+1,node.right) # same with the right child
        
        # when recursive calls finish will return res to levelOrder() which will return it as the answer
        return res
