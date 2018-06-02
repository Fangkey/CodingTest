# coding=utf-8

# 2018-06-03 00:29
# 2018-06-03 00:31
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None:
            return

        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)

# 2018-06-02 19:04
# 2018-06-02 19:16

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ret = []
        stack = [root]
        visited_set = set()
        while stack:
            l = stack[-1].left
            r = stack[-1].right

            if (l is None or l in visited_set) and (r is None or r in visited_set):
                ret.append(stack[-1].val)
                visited_set.add(stack[-1])
                stack.pop()
            else:
                if r is not None:
                    stack.append(r)
                if l is not None:
                    stack.append(l)
        return ret

