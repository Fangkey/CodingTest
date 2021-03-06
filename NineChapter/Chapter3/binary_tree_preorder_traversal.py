from binary_search_tree import BinarySearchTree, TreeNode

class Solution1(object):
    def helper(self, root, result):
        if root is not None:
            v = root.val
            result.append(v)
            self.helper(root.left, result)
            self.helper(root.right, result)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result


#2018-05-07 23:54
#2018-05-07 23:57

class Solution(object):
    def helper(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result


if __name__ == "__main__":
    bt = BinarySearchTree()
    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)

    s = Solution()
    preorder = s.preorderTraversal(root)
    print preorder
