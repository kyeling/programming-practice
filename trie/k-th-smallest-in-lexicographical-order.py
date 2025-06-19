class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if n < 10: 
            return k
        
        n_str = str(n)
        current_num, k_remaining = self.findSubtree(n_str, k, 1)
        while k_remaining > 0:
            # current_num is the prefix/subtree to search, x10 to go down a level into subtree
            current_num, k_remaining = self.findSubtree(n_str, k_remaining, current_num * 10)
        return current_num

    def findSubtree(self, n_str: str, k: int, root: int) -> tuple[int, int]:
        # if k is 1, return the current number (root)
        if k == 1: 
            return root, 0
        
        depth = len(n_str) # the digit count of n gives the max depth of the trie
        level = len(str(root)) # the digit count of the current number gives the current level

        # if we've reached the bottom level of trie, there are no child nodes, only sibling nodes
        # (subtract 1 to count traversal of the current_number)
        if level == depth: 
            return root + k - 1, 0

        # otherwise, each subtree at the current level is bounded by the following sizes
        # example:  depth=3, level=2 --> subtree size range is [1, 11] 
        #           depth=3, level=1 --> subtree size range [11, 111]
        lower_bound = int('1' * (depth-level))
        upper_bound = int('1' * (depth-level+1))

        # the leading digits of n tell us where the first non-full subtree is and 
        # the remaining digits of n tell us how many nodes are in that subtree
        leading_digits = int(n_str[:level])
        remaining_digits = int(n_str[level:]) if n_str[level:] else 0

        k_remaining = k
        for prefix in range(root, (root + 10)//10*10):
            if prefix < leading_digits:
                subtree_size = upper_bound
            elif prefix > leading_digits:
                subtree_size = lower_bound
            else:
                subtree_size = lower_bound + remaining_digits + 1
            
            if k_remaining > subtree_size:
                k_remaining -= subtree_size
            else:
                return prefix, k_remaining - 1
