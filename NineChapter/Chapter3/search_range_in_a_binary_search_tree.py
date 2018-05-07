from binary_search_tree import BinarySearchTree, TreeNode, build_tree


class Solution1(object):
    def helper(self, root, a, b, result):
        if root is None:
            return

        self.helper(root.left, a, b, result)
        if root.val >=a and root.val <= b:
            result.append(root.val)
        self.helper(root.right, a, b, result)

    def searchRange(self, root, a, b):
        result = []
        self.helper(root, a, b, result)

        return result

# 2018-05-08 00:31
# 2018-05-08 00:38

class Solution(object):
    def helper(self, root, a, b, result):
        if root is None:
            return

        v = root.val
        if v >= a:
            self.helper(root.left, a, b, result)

        if v >= a and v <= b:
            result.append(v)

        if v <= b:
            self.helper(root.right, a, b, result)


    def searchRange(self, root, a, b):
        result = []
        self.helper(root, a, b, result)
        return result



if __name__ == "__main__":
    bt = BinarySearchTree()
    s = Solution()

    nums = [2, 1, 4, 6, 2, 3, 6]
    root = bt.build_binary_search_tree(nums)
    # 4
    print s.searchRange(root, 3, 6)

    nums = [2, 1]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.searchRange(root, 1, 2)
    print s.searchRange(root, 3, 4)
    print s.searchRange(root, 0, 1)



    nums = [2, 1, 3, 4, 5]
    root = bt.build_binary_search_tree(nums)
    # 2
    print s.searchRange(root, 1, 5)