bool isBalanced(struct TreeNode* root){
    if(root == NULL) return true;
    return abs(maxDepth(root->left) - maxDepth(root->right)) <= 1 
        && isBalanced(root->left) && isBalanced(root->right);
}

int maxDepth(struct TreeNode* t){
    if(t == NULL) return 0;
    return 1 + max(maxDepth(t->left), maxDepth(t->right));
}

int max(int (*a)(struct TreeNode*), int (*b)(struct TreeNode*)){
    if (*a > *b) return *a;
    return *b;
}
