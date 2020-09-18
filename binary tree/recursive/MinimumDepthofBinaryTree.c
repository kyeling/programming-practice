int max(int (*a)(struct TreeNode*), int (*b)(struct TreeNode*)){
    if(*a > *b) return *a;
    return *b;
}

int maxDepth(struct TreeNode* root){
    if(root == NULL) return 0;   
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
