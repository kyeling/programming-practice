bool hasPathSum(struct TreeNode* root, int sum){
    if(root == NULL) return false;
    if(root->left == NULL && root->right == NULL){
        if(root->val == sum) {
            return true;
        }
        return false;
    } 
    return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
}
