class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.helper(s, [], 0, result)
        ret_strings = []
        for p in result:
            start = 0
            one_partition = []
            for i in p:
                cur_str = s[start: i]
                one_partition.append(cur_str)
                start = i
            ret_strings.append(one_partition)
        return ret_strings

    def is_palindrome(self, s):
        s_len = len(s)
        for i in range(0, s_len / 2):
            if s[i] != s[s_len -1 - i]:
                return False
        return True

    def helper(self, s, cur_partitions, cur_index, result):
        if len(cur_partitions) == 0:
            last_partition = 0
        else:
            last_partition = cur_partitions[-1]

        if cur_index == len(s):
            result.append(cur_partitions[:])
            return

        for i in range(cur_index, len(s)):
            cur_part_s = s[last_partition: i + 1]
            if self.is_palindrome(cur_part_s):
                cur_partitions.append(i + 1)
                self.helper(s, cur_partitions, i + 1, result)
                cur_partitions.pop()


if __name__ == "__main__":
    s = Solution()
    print s.partition('aab')