from binary_search_tree import BinarySearchTree, TreeNode, build_tree

class Solution(object):
    def helper(self, root, result):
        if root is None:
            return

        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.helper(root, result)

        if len(result) <= 1:
            return True
        else:
            for i in range(0, len(result) - 1):
                if result[i + 1] <= result[i]:
                    return False
            return True




if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    tree_nodes = [10, 5, 15, None, None, 6, 20]
    root = build_tree(tree_nodes)
    print s.isValidBST(root)

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    root.val = 1
    # 2
    print s.isValidBST(root)

    nums = [1, 2]
    root = bt.build_binary_search_tree(nums)
    # 1
    print s.isValidBST(root)

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 4
    print s.isValidBST(root)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.isValidBST(root)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.isValidBST(root)