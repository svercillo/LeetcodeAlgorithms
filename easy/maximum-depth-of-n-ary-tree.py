/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int maxDepth(Node* root) {

        vector<Node*> q;         

        q.push_back(root);
        if (! root) {
            return 0;
        }
        int depth = 0;
        int i = 0;
        while (i <  q.size() ){
            int current_qsize = q.size();
            for (; i< current_qsize; i++){
                for (auto& it : q[i]->children){
                    q.push_back(it);
                }
            }

            depth += 1;
        }

        return depth;
    }
};
