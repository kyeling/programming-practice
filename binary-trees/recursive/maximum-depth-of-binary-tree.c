int max(int (*a)(struct TreeNode*), int (*b)(struct TreeNode*)){
    if(*a > *b) return *a;
    return *b;
}

int maxDepth(struct TreeNode* root){
    if(root == NULL) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

/**
options:
- traverse every path and keep track of max length
- recursion: if leaf, add 1, else take max of left and right subtrees

the following don't work bc tree isn't balanced:
- convert to array and use log on length of array
- push all elements into a queue/linked list and use size()
- recursion with static variable?
**/
