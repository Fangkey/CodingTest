from binary_search_tree import BinarySearchTree, TreeNode, build_tree


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return False

        return True

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None

        cur_node = self.stack.pop()
        ret_val = cur_node.val

        if cur_node.right is not None:
            self.stack.append(cur_node.right)
            node = cur_node.right.left
            while node is not None:
                self.stack.append(node)
                node = node.left

        return ret_val

if __name__ == "__main__":
    bt = BinarySearchTree()

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [1, 2]
    root = bt.build_binary_search_tree(nums)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1, 3]
    root = bt.build_binary_search_tree(nums)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v

    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print v