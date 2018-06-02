# coding=utf-8

# 2018-06-03 00:27
# 2018-06-03 00:29

class Solution(object):
    def inorderTraversal(self, root):
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
        result.append(root.val)
        self.helper(root.right, result)



# 2018-06-02 19:17
# 2018-06-02 19:28

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
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
            if l not in visited and l is not None:
                stack.append(l)
            else:
                ret.append(stack[-1].val)
                visited.add(stack[-1])
                stack.pop()
                if r is not None:
                    stack.append(r)

        return ret