class Solution {
public:
    unordered_map<int, Node*> seen;
    
    Node* cloneGraph(Node* node) {  
        if(node == nullptr) return nullptr; // add this condition to prevent null obj access, e.g. node->val
        if(!seen.empty() && seen[node->val] != nullptr) {
            // if node has already been cloned, return clone
            return seen[node->val];
        }
        // otherwise, create a new node, insert into map, and append clones of neighbors
        Node* clone = new Node(node->val);
        seen[node->val] = clone;
        
        for(Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return clone;        
    }
};
