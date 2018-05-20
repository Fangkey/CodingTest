# coding=utf-8

# convert a binary tree to a circled double linked list, in the order of in-order traversal
# do not allocate any new node, use left as prev, right as next

# 2018-05-19 22:33
# 2018-05-19 23:06

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def ConvertBTtoCircledDBLL(self, root):
        if root is None:
            return root

        l_head = self.ConvertBTtoCircledDBLL(root.left)
        r_head = self.ConvertBTtoCircledDBLL(root.right)

        if l_head is None:
            l_head = root
            l_head.right = l_head
            l_head.left = l_head
            l_tail = l_head
        else:
            l_tail = l_head.left
            l_tail.right = root
            root.left = l_tail
            l_tail = root

        if r_head is None:
            l_tail.right = l_head
            l_head.left = l_tail
        else:
            r_tail = r_head.left
            l_tail.right = r_head
            r_head.left = l_tail
            r_tail.right = l_head
            l_head.left = r_tail

        return l_head

if __name__ == "__main__":
    s = Solution()

    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n0.left = n1
    n0.right = n2

    n1.left = n3
    n1.right = n4

    n2.left = n5
    n5.right = n6

    head = s.ConvertBTtoCircledDBLL(n0)
    list_cw = []
    for i in range(0, 7):
        list_cw.append(head.val)
        head = head.right

    list_ccw = []
    for i in range(0, 7):
        list_ccw.append(head.val)
        head = head.left

    print list_cw
    print list_ccw