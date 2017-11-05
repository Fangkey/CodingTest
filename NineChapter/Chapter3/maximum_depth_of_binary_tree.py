from binary_search_tree import BinarySearchTree, TreeNode

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        return max(l_depth, r_depth) + 1


if __name__ == "__main__":
    bt = BinarySearchTree()
    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)

    s = Solution()
    print s.maxDepth(root)

    print s.maxDepth(None)