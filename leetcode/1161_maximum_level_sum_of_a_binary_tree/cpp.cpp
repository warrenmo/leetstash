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
    int maxLevelSum(TreeNode const* const root) {
        int max_sum = INT_MIN;
        int min_level = INT_MAX;

        std::vector<TreeNode const*> level = { root };
        std::vector<TreeNode const*> next_level = {};

        for (int curr_level = 1; !level.empty(); ++curr_level) {
            int curr_sum = 0;
            next_level.clear();
            for (auto node : level) {
                curr_sum += node->val;
                if (node->left) next_level.push_back(node->left);
                if (node->right) next_level.push_back(node->right);
            }
            if (curr_sum > max_sum) {
                max_sum = curr_sum;
                min_level = curr_level;
            }
            std::swap(level, next_level);
        }
        
        return min_level;
    }
};
