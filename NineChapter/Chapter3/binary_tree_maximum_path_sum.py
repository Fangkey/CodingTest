from binary_search_tree import BinarySearchTree, TreeNode
import sys

class Solution(object):
    def helper(self, root):
        if root is None:
            return -sys.maxint, -sys.maxint

        l_to_node_max, l_path_max = self.helper(root.left)
        r_to_node_max, r_path_max = self.helper(root.right)

        to_node_max = max(l_to_node_max + root.val,
                          r_to_node_max + root.val,
                          root.val
                          )
        cur_path_max = max(l_to_node_max + r_to_node_max + root.val,
                           l_to_node_max + root.val,
                           r_to_node_max + root.val,
                           root.val)
        path_max = max(cur_path_max,
                       l_path_max,
                       r_path_max)

        return to_node_max, path_max

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        to_node_max, path_max = self.helper(root)
        return path_max

if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [-2, 1]
    root = bt.build_binary_search_tree(nums)
    # 1
    print s.maxPathSum(root)

    nums = [2, -1]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.maxPathSum(root)

    nums = [-3]
    root = bt.build_binary_search_tree(nums)
    # -3
    print s.maxPathSum(root)

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 21
    print s.maxPathSum(root)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    # 6
    print s.maxPathSum(root)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 15
    print s.maxPathSum(root)

    nums = [2, 1, -3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 12
    print s.maxPathSum(root)