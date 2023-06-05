Select tags
0/5
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dfs(TreeNode * node, unordered_map<int, int> *freq){ 
        if (node == nullptr){
            return 0;
        }

        int sum = node->val;
        if (node->left){
            sum += dfs(node->left, freq);
        }

        if (node->right){
            sum += dfs(node->right, freq);
        }

        if (freq->find(sum) == freq->end()){ 
            (*freq)[sum] = 0;
        }
        (*freq)[sum] += 1;

        // cout << sum << " " << freq[sum] << endl;

    
        return sum;
    }

    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int, int> freq;

        this->dfs(root, &freq);


        int most_freq = -1;
        for (auto entry : freq){ 

            cout << entry.first << " :  " << entry.second << endl;
            if (most_freq == -1  || entry.second > freq[most_freq]){
                most_freq = entry.first;
            }
        }      

        cout << most_freq << endl;
        vector<int> result;
        for (auto entry : freq){ 
            if (entry.second == freq[most_freq]){
                result.push_back(entry.first);
            }
        }

        return result;
    }
    
};
