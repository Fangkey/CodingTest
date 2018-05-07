from binary_search_tree import BinarySearchTree, TreeNode

from collections import deque

class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        q_size = len(queue)
        result = []
        while len(queue) != 0:
            l = []
            for i in range(0, q_size):
                cur_root = queue.popleft()
                if cur_root is not None:
                    l.append(cur_root.val)
                    queue.append(cur_root.left)
                    queue.append(cur_root.right)
            if len(l) != 0:
                result.append(l)
            q_size = len(queue)

        result.reverse()
        return result


# 2018-05-07 23:23
# 2018-05-07 23:30

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        if root is None:
            return []

        q = deque([])
        q.append(root)

        result = []
        while len(q) != 0:
            size = len(q)
            level = []
            for i in range(0, size):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            result.append(level)

        result.reverse() # is not reversed(result), it returns an iter
        return result


if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    print s.levelOrderBottom(root)

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    print s.levelOrderBottom(root)

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    print s.levelOrderBottom(root)

    nums = [3, 2, 1, 4, 5]
    root = bt.build_binary_search_tree(nums)
    print s.levelOrderBottom(root)