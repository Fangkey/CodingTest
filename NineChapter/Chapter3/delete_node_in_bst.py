from binary_search_tree import BinarySearchTree, TreeNode, build_tree
from binary_search_tree_iterator import BSTIterator

class Solution(object):
    def findNode(self, root, key):
        parent = None
        left = False
        while root is not None:
            if root.val > key:
                parent = root
                root = root.left
                left = True
            elif root.val < key:
                parent = root
                root = root.right
                left = False
            else:
                return root, parent, left

        return None, None, False

    def findMax(self, root):
        while root is not None:
            if root.right is None:
                return root
            else:
                root = root.right

        return None

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node_del, parent, left = self.findNode(root, key)

        if node_del is None:
            return root

        left_max = self.findMax(node_del.left)
        if left_max is None:
            if parent is None:
                return node_del.right
            if left:
                parent.left = node_del.right
            else:
                parent.right = node_del.right
        else:
            left_new_root = self.deleteNode(node_del.left, left_max.val)
            left_max.left = left_new_root
            left_max.right = node_del.right
            if parent is None:
                return left_max
            if left:
                parent.left = left_max
            else:
                parent.right = left_max

        return root


if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [1]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 1)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v


    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 4)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 2)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [1, 2]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 1)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 3)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    root = s.deleteNode(root, 1)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v