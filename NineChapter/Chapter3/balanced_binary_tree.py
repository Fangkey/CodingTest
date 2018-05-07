from binary_search_tree import BinarySearchTree, TreeNode

class Solution1(object):
    def helper(self, root):
        if root is None:
            return True, 0

        l_is_balanced, l_depth = self.helper(root.left)
        r_is_balanced, r_depth = self.helper(root.right)
        return l_is_balanced and r_is_balanced and abs(l_depth - r_depth) <= 1, max(l_depth, r_depth) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, depth = self.helper(root)
        return is_balanced



# 2018-05-07 23:59
# 2018-05-08 0:03

class Solution(object):
    def helper(self, root):
        # if is balanced, return height, else return -1
        if root is None:
            return 0

        l = self.helper(root.left)
        r = self.helper(root.right)

        if l != -1 and r != -1 and abs(l - r) <= 1:
            return max(l, r) + 1
        else:
            return -1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not self.helper(root) == -1



if __name__ == "__main__":
    bt = BinarySearchTree()
    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)

    s = Solution()
    print s.isBalanced(root)

    print s.isBalanced(None)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    print s.isBalanced(root)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    print s.isBalanced(root)