bool helper(struct TreeNode* left, struct TreeNode* right) {
    if (left == NULL && right == NULL) {
        return true;
    } else if (left == NULL || right == NULL) {
        return false;
    } else {
        if (left->val == right->val) {
            if (helper(left->left, right->right) && helper(left->right, right->left)) {
                return true;
            }
        }
    }
    return false; 
}

bool isSymmetric(struct TreeNode* root){
    bool (*function_ptr)(struct TreeNode*, struct TreeNode*) = &helper;
    if(root == NULL) {
        return true;
    }
    return (*function_ptr)(root->left, root->right);
}
