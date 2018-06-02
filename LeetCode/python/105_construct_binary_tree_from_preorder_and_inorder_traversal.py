# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2018-06-03 00:35
# 2018-06-03 00:57

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        cur_root_index = [0]
        root = self.helper(preorder, cur_root_index, inorder)
        return root

    def helper(self, preorder, cur_index, inorder):
        if cur_index[0] == len(preorder) or len(inorder) == 0:
            return None

        cur_root_val = preorder[cur_index[0]]
        root = TreeNode(cur_root_val)
        root_index = inorder.index(cur_root_val)
        cur_index[0] += 1
        left = self.helper(preorder, cur_index, inorder[0: root_index])
        right = self.helper(preorder, cur_index, inorder[root_index + 1: ])

        root.left = left
        root.right = right
        return root

if __name__ == "__main__":
    s = Solution()
    root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print root