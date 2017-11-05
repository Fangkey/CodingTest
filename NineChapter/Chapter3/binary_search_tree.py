class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def insert_into_binary_search_tree(self, root, n):
        if root is None:
            return TreeNode(n)
        else:
            v = root.val
            if n < v:
                if root.left is None:
                    root.left = TreeNode(n)
                else:
                    self.insert_into_binary_search_tree(root.left, n)
            else:
                if root.right is None:
                    root.right = TreeNode(n)
                else:
                    self.insert_into_binary_search_tree(root.right, n)
        return root

    def build_binary_search_tree(self, nums):
        if len(nums) == 0:
            return None

        root = None
        for n in nums:
            root = self.insert_into_binary_search_tree(root, n)

        return root

def build_tree(node_list):
    if len(node_list) == 0:
        return None

    tree_nodes = []
    for node in node_list:
        if node is not None:
            tree_node = TreeNode(node)
        else:
            tree_node = None

        tree_nodes.append(tree_node)

    for i, node in enumerate(tree_nodes):
        left_index = i * 2 + 1
        right_index = i * 2 + 2
        if left_index < len(tree_nodes):
            node.left = tree_nodes[left_index]
        if right_index < len(tree_nodes):
            node.right = tree_nodes[right_index]

    return tree_nodes[0]