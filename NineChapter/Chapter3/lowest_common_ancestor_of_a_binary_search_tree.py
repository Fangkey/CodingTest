# 2017-09-25 0:38
from binary_search_tree import BinarySearchTree, TreeNode

class Solution(object):
    def find_path(self, root, n):
        result = []
        while root is not None:
            v = root.val
            if n < v:
                result.append(root)
                root = root.left
            elif n > v:
                result.append(root)
                root = root.right
            else:
                result.append(root)
                return True, result
        return False, []

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        found_p, p_path = self.find_path(root, p)
        if not found_p:
            return None

        found_q, q_path = self.find_path(root, q)
        if not found_q:
            return None

        common_len = 0
        for i in range(0, min(len(p_path), len(q_path))):
            if p_path[i].val == q_path[i].val:
                common_len += 1
            else:
                break

        return p_path[common_len - 1]

# 2018-05-08-00:20
# 2018-05-08-00:26

class Solution(object):
    def helper(self, root, p, q):
        if root is None or root is p or root is q:
            return root

        l = self.helper(root.left, p, q)
        r = self.helper(root.right, p, q)

        if l is not None and r is not None:
            return root
        if l is not None:
            return l
        if r is not None:
            return r

        return None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root, p, q)

if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 2, 1).val

    nums = [1, 2]
    root = bt.build_binary_search_tree(nums)
    # 1
    print s.lowestCommonAncestor(root, 2, 1)

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 4
    print s.lowestCommonAncestor(root, 3, 6)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 1, 3)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.lowestCommonAncestor(root, 1, 4)