class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []

        result = []
        self.helper(s, [], 0, result)
        ret_ips = []
        for p in result:
            ip = []
            start = 0
            for i in p:
                seg = s[start: i]
                ip.append(seg)
                start = i
            ip.append(s[p[-1]:])
            ret_ips.append('.'.join(ip))
        return ret_ips

    def is_valid_seg(self, seg):
        int_seg = int(seg)
        if len(seg) != len(str(int_seg)):
            return False

        if int_seg >= 0 and int_seg <= 255:
            return True
        else:
            return False

    def helper(self, s, cur_partitions, cur_index, result):
        if len(cur_partitions) == 3:
            cur_seg = s[cur_partitions[-1]: ]
            if self.is_valid_seg(cur_seg):
                valid_partitions = cur_partitions[:]
                result.append(valid_partitions)
            return

        if len(cur_partitions) == 0:
            last_partition = 0
        else:
            last_partition = cur_partitions[-1]

        for i in range(cur_index, len(s) - 1):
            cur_seg = s[last_partition: i + 1]
            if self.is_valid_seg(cur_seg):
                cur_partitions.append(i + 1)
                self.helper(s, cur_partitions, i + 1, result)
                cur_partitions.pop()



if __name__ == "__main__":
    s = Solution()
    print s.restoreIpAddresses('0000')
    print s.restoreIpAddresses('010010')
    print s.restoreIpAddresses('25525511135')