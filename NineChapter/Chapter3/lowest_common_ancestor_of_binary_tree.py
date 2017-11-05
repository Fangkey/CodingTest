from binary_search_tree import BinarySearchTree, TreeNode

# 是否一定存在解，对问题的解法影响很大
class Solution(object):
    def helper(self, root, p, q):
        if root is None:
            return False, False, root

        left_has_p, left_has_q, left_node = self.helper(root.left, p, q)
        right_has_p, right_has_q, right_node = self.helper(root.right, p, q)

        if left_node is not None:
            return True, True, left_node
        if right_node is not None:
            return True, True, right_node

        if left_has_p or right_has_p or root.val == p:
            has_p = True
        else:
            has_p = False

        if left_has_q or right_has_q or root.val == q:
            has_q = True
        else:
            has_q = False

        if has_p and has_q:
            ret_node = root
        else:
            ret_node = None

        return has_p, has_q, ret_node

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        has_p, has_q, node = self.helper(root, p, q)
        return node
        if node is not None:
            return node.val
        else:
            return "None"

if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 4
    print s.lowestCommonAncestor(root, 3, 6)

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 4
    print s.lowestCommonAncestor(root, 3, 7)

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 2, 1)

    nums = [1, 2]
    root = bt.build_binary_search_tree(nums)
    # 1
    print s.lowestCommonAncestor(root, 2, 1)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 1, 3)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 1, 4)