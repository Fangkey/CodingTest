class Solution(object):
    def findKth(self, nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0:
            return nums2[k - 1]
        if len2 == 0:
            return nums1[k - 1]

        start1 = 0
        start2 = 0
        rest = k
        while True:
            if start1 >= len1:
                return nums2[start2 + rest - 1]
            elif start2 >= len2:
                return nums1[start1 + rest - 1]

            cur_mid = rest / 2
            if start1 + cur_mid <= len1 and start2 + cur_mid <= len2:
                if rest == 1:
                    if nums1[start1] > nums2[start2]:
                        return nums2[start2]
                    else:
                        return nums1[start1]

                m1 = nums1[start1 + cur_mid - 1]
                m2 = nums2[start2 + cur_mid - 1]
                if m1 > m2:
                    start2 += cur_mid
                else:
                    start1 += cur_mid
                rest -= cur_mid
            else:
                if start1 + cur_mid > len1:
                    start2 += cur_mid
                    rest -= cur_mid
                elif start2 + cur_mid > len2:
                    start1 += cur_mid
                    rest -= cur_mid


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        if (len1 + len2) % 2 == 1:
            return self.findKth(nums1, nums2, (len1 + len2) / 2 + 1)
        else:
            return float(self.findKth(nums1, nums2, (len1 + len2) / 2) +
                    self.findKth(nums1, nums2, (len1 + len2) / 2 + 1)) / 2


if __name__ == "__main__":
    s = Solution()
    nums1 = [4]
    nums2 = [1, 2, 3, 5, 6]
    3.5
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    # 2.5
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [3, 4]
    nums2 = [1, 2]
    # 2.5
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    # 2
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 1, 1, 1, 3, 3]
    nums2 = [1, 1, 3, 3, 3]
    # 1
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 1, 3, 3]
    nums2 = [1, 1, 3, 3]
    # 2
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1]
    nums2 = [1, 1, 2, 2, 3, 3]
    # 2
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1]
    nums2 = [1, 1, 3, 3]
    # 1
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 1, 3, 3]
    nums2 = [1]
    # 1
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = []
    nums2 = [1, 1, 3, 3]
    # 2
    print s.findMedianSortedArrays(nums1, nums2)

    s = Solution()
    nums1 = [1, 1, 3, 3]
    nums2 = []
    # 2
    print s.findMedianSortedArrays(nums1, nums2)

