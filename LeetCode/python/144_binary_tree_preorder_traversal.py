# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2018-06-03 00:22
# 2018-06-03 00:26
class Solution1(object):
    def preorderTraversal(self, root):
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

        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)


# 2018-06-02 19:30
# 2018-06-02 19:43
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ret = []
        visited = set()
        stack = [root]

        while stack:
            l = stack[-1].left
            r = stack[-1].right
            if stack[-1] not in visited:
                visited.add(stack[-1])
                ret.append(stack[-1].val)
                if l is not None and l not in visited:
                    stack.append(l)
            else:
                if r is not None and r not in visited:
                    stack.append(r)
                else:
                    stack.pop()
        return ret