/*
 * LeetCode: 5. LongestPalindromicSubstring
 * Finish Time: 2017.11.11 23:18
 * Time: 25min
 * Wrong Submissions: 2, one substring param error, one time limit exceeded
 * Tip: do not get substring, pass s, start, end to isPalindrome
 */

class Solution5 {
	public boolean isPalindrome(String s, int start, int end) {
		for (int i = 0; i < (end - start + 1) / 2; i++) {
			if (s.charAt(start + i) != s.charAt(end - i)) {
				return false;
			}
		}
		return true;
	}
	
    public String longestPalindrome(String s) {
    	if (s.length() == 0) {
    		return "";
    	}
    	
    	int maxLen = 1;
    	String longest = s.substring(0, 1);
        for (int i = 0; i < s.length(); i++) {
        	// Important, pass len < max_len
        	for (int j = i + maxLen ; j < s.length(); j++) {
        		if (this.isPalindrome(s, i, j)) {
        			if ((j - i + 1) > maxLen) {
        				maxLen = j - i + 1;
        				longest = s.substring(i, j + 1);
        			}
        		}
        	}
        }
        return longest;
    }
    
    public static void main(String[] args) {
    	Solution5 s = new Solution5();
    	
    	String input;
    	String output;
    	
    	// bb
    	input = "cbbd";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    	
    	//a
    	input = "a";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    	
    	// bab
    	input = "babad";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    }
}


/*
 * LeetCode: 5. LongestPalindromicSubstring
 * Finish Time: 2017.11.11 23:55
 * Time: 20min
 * Wrong: Time limit exceeded
 * Tip: Another way to calculate palindrome, from center to start and end
 */
class Solution5_2 {
    public String longestPalindrome(String s) {
    	if (s.length() == 0) {
    		return "";
    	}
    	
    	int maxLength = 1;
    	String longest = s.substring(0, 1);
    	
    	for (int i = 0; i < s.length(); i++) {
    		int count = 1;
    		while(i - count >= 0 && i + count < s.length() && s.charAt(i - count) == s.charAt(i + count)) {
    			count++;
    		}
    		count--;
    		if (count * 2 + 1 > maxLength) {
    			maxLength = count * 2 + 1;
    			longest = s.substring(i - count, i + count + 1);
    		}
    		
    		count = 1;
    		while(i - count + 1 >= 0 && i + count < s.length() && s.charAt(i - count + 1) == s.charAt(i + count)) {
    			count++;
    		}
    		count--;
    		if (count * 2 > maxLength) {
    			maxLength = count * 2;
    			longest = s.substring(i - count + 1, i + count + 1);
    		}
    	}
    	return longest;
    }
    
    public static void main(String[] args) {
    	Solution5 s = new Solution5();
    	
    	String input;
    	String output;
    	
    	// bb
    	input = "bb";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    	
    	// bb
    	input = "cbbd";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    	
    	//a
    	input = "a";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    	
    	// bab
    	input = "babad";
    	output = s.longestPalindrome(input);
    	System.out.println(output);
    }
}

