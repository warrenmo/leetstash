# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -inf
        min_level = inf
        level = [root]
        next_level = []
        curr_level = 1

        while (len(level)):
            curr_sum = 0
            next_level.clear()

            for node in level:
                curr_sum += node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                min_level = curr_level

            curr_level += 1
            level, next_level = next_level, level

        return min_level
