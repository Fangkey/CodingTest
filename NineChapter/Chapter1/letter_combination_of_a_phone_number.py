class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        dail_pad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []
        self.helper(dail_pad, digits, [], 0, result)
        return result


    def helper(self, dail_pad, digits, cur_comb, cur_index, result):
        if cur_index == len(digits):
            result.append(''.join(cur_comb))
            return

        cur_digit = digits[cur_index]
        if cur_digit not in dail_pad:
            return

        cur_letter_list = dail_pad[digits[cur_index]]
        for d in cur_letter_list:
            cur_comb.append(d)
            self.helper(dail_pad, digits, cur_comb, cur_index + 1, result)
            cur_comb.pop()

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations('23')