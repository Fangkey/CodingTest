# coding=utf-8

# 2018-05-17 13:22
# 2018-05-17 13:15 TLE

class Solution1(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        start_dict = {}
        word_set = set(words)
        for w in word_set:
            beg = 0
            while True:
                i = s.find(w, beg)
                if i == -1:
                    break
                beg = i + 1
                
                w_list = start_dict.get(i, [])
                w_list.append((w, len(w)))
                start_dict[i] = w_list
        
        wc_dict = {}
        for w in words:
            wc_dict[w] = wc_dict.get(w, 0) + 1
        
        result = []
        
        for i in start_dict.keys():
            self.helper(start_dict, i, [], wc_dict, result)
        return result
    
    
    def helper(self, start_dict, cur_i, index_list, wc_dict, result):
        if sum(wc_dict.values()) == 0:
            result.append(min(index_list))
            return
        
        if cur_i not in start_dict:
            return
        
        cur_word_list = start_dict[cur_i]
        for w in cur_word_list:
            if wc_dict[w[0]] == 0:
                continue
            
            wc_dict[w[0]] -= 1
            index_list.append(cur_i)
            self.helper(start_dict, cur_i + w[1], index_list, wc_dict, result)
            wc_dict[w[0]] += 1
            index_list.pop()
            

# 2018-05-17 13:32 LTE
# 2018-05-17 15:19
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        
        wc_dict = {}
        for w in words:
            wc_dict[w] = wc_dict.get(w, 0) + 1
        w_cnt = len(words)
        w_len = len(words[0])
        
        result = []
        for i in range(0, len(s) - w_len * w_cnt + 1): # important to reduce loop time for TLE
            cur_wc = {}
            cnt = 0
            start = i
            cur_i = start
            while True:
                sub_str = s[cur_i: cur_i + w_len]
                if not sub_str in words:
                    break
                wc = cur_wc.get(sub_str, 0)
                if wc + 1 > wc_dict[sub_str]:
                    break
                cur_wc[sub_str] = wc + 1
                cnt += 1
                cur_i += w_len
                
                if cnt == w_cnt:
                    result.append(start)
                    break
                
                if cur_i >= len(s):
                    break
            
        return result
            
if __name__ == "__main__":
    s = Solution()

    str = ""
    words = []
    print s.findSubstring(str, words)
    
    str = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print s.findSubstring(str, words)
    
    
    str = "barfoothefoobarman"
    words = ["foo","bar"]
    print s.findSubstring(str, words)
    
    
    str = "wordgoodstudentgoodword"
    words = ["word","student"]
    print s.findSubstring(str, words)