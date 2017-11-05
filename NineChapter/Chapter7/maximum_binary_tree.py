# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0:
            return None

        nums.append(sys.maxint)

        node_list = []
        for n in nums:
            node_list.append(TreeNode(n))

        stack = []
        stack.append(node_list[0])

        for node in node_list[1:]:
            if node.val > stack[-1].val:
                right_list = []
                while len(stack) != 0 and stack[-1].val < node.val:
                    right_list.append(stack.pop())

                if len(right_list) == 1:
                    node.left = right_list[0]
                    stack.append(node)
                else:
                    child = right_list[0]
                    for i in range(1, len(right_list)):
                        right_list[i].right = child
                        child = right_list[i]

                    node.left = child
                    stack.append(node)
            else:
                stack.append(node)

        return node_list[-1].left


if __name__ == "__main__":
    s = Solution()

    print s.constructMaximumBinaryTree([3])

    print s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])



