# coding=utf8
# 2018-05-05 01:41
# 2018-05-05 02:24 Heap

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = nums[0: k]
        # build heap
        def heapify(h, i):
            while i < k / 2:
                m = i
                l = i * 2 + 1
                r = i * 2 + 2
                if l < k and h[l] < h[i]:
                    m = l

                if r < k and h[r] < h[m]:
                    m = r

                if m == i:
                    break

                h[m], h[i] = h[i], h[m]
                i = m

        for i in range((k - 1) / 2, -1, -1):
            heapify(h, i)

        for n in nums[k:]:
            if n < h[0]:
                continue
            h[0] = n
            heapify(h, 0)

        return h[0]


if __name__ == "__main__":
    s = Solution()

    # 5
    print s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    # 4
    print s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)



