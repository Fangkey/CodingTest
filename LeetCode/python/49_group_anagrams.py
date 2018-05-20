# coding=utf-8

# 2018-05-20 04:17
# 2018-05-20 04:21

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = dict()
        for s in strs:
            ss = "".join(sorted(s))
            l = anagram.get(ss, [])
            l.append(s)
            anagram[ss] = l
        return anagram.values()


if __name__ == "__main__":
    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print s.groupAnagrams(strs)
