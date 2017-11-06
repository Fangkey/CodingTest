import java.util.HashSet;

/*
 * LeetCode: 3. Longest Substring Without Repeating Characters
 * Finish Time: 2017.11.07 1:33
 * Time: 28min
 * Wrong Submissions: 3 
 */
class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        int max_length = 0;
        HashSet<Character> char_set = new HashSet<Character>();
        for (int i = 0; i < s.length(); i++) {
        	char_set.clear();
        	for (int j = i; j < s.length(); j++) {
        		if (char_set.contains(s.charAt(j))) {
        			if (char_set.size() > max_length) {
        				max_length = char_set.size();
        			}
        			// Wrong 3
        			break;
        		} else {
            		char_set.add(s.charAt(j));
            		// Wrong 2
            		if (j == s.length() - 1) {
            			if (char_set.size() > max_length) {
            				max_length = char_set.size();
            			}
            		}
        		}
        	}
        }
        
        // Wrong 1
        if (char_set.size() > max_length) {
        	max_length = char_set.size();
        }
        return max_length;
    }
    
    public static void main(String[] args) {
    	Solution3 s = new Solution3();
    	
    	String str;
    	int len;
    	
    	// 4
    	str = "jbpnbwwd";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    	
    	// 2
    	str = "au";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    	
    	// 3
    	str = "abcabcbb";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    	
    	// 1
    	str = "bbbbb";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    	
    	// 3
    	str = "pwwkew";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    	
    	// 1
    	str = "c";
    	len = s.lengthOfLongestSubstring(str);
    	System.out.println(len);
    }
}