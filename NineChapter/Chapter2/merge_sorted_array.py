class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 and i2 >= 0:
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n2 > n1:
                nums1[i1 + i2 + 1] = n2
                i2 -= 1
            else:
                nums1[i1 + i2 + 1] = n1
                i1 -= 1

        if i2 >= 0:
            while i2 >= 0:
                nums1[i2] = nums2[i2]
                i2 -= 1




if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 1, 3, 3, 0, 0, 0, 0, 0, 0]
    nums2 = [1, 1, 3, 3]
    print s.merge(nums1, 4, nums2, 4)
    print nums1

    nums1 = [0, 0, 0, 0, 0, 0]
    nums2 = [1, 1, 3, 3]
    print s.merge(nums1, 0, nums2, 4)
    print nums1

    nums1 = [1, 1, 3, 3, 0, 0]
    nums2 = []
    print s.merge(nums1, 0, nums2, 0)
    print nums1

    nums1 = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
    nums2 = [5, 6, 7, 8]
    print s.merge(nums1, 4, nums2, 4)
    print nums1

    nums1 = [5, 6, 7, 8, 0, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 4]
    print s.merge(nums1, 4, nums2, 4)
    print nums1