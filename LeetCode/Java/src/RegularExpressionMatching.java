/*
 * LeetCode: 10. Regular Expression Matching
 * Finish Time: 2017.11.15 02:04
 * Time: 49min, 31min think and see the answer, 18min implement
 * Wrong Submissions: 0
 * Tip: Multi-Recursion
 */

class Solution10 {
    public boolean isMatch(String s, String p) {
    	// Important. Using isEmpty() instead of p.length() == 0 
    	// Important. One Ending condition.
        if (p.isEmpty()) {
        	return s.isEmpty();
        }
        
        // Important. !s.isEmpty()
        boolean fisrtMatch = !s.isEmpty()
        		&& (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.');
        
        if (p.length() >= 2 && p.charAt(1) == '*') {
        	// Important. Multi-Recursion
        	return fisrtMatch && this.isMatch(s.substring(1), p) || 
        			this.isMatch(s, p.substring(2));
        } else {
        	return fisrtMatch && this.isMatch(s.substring(1), p.substring(1));
        }
    }
    
    public static void main(String[] args) {
    	Solution10 s = new Solution10();

    	// false
    	System.out.println(s.isMatch("aa", "a"));
    	
    	// true
    	System.out.println(s.isMatch("aa", "aa"));
    	
    	// false
    	System.out.println(s.isMatch("aaa", "aa"));
    	
    	// true
    	System.out.println(s.isMatch("aa", "a*"));

    	// true
    	System.out.println(s.isMatch("aa", ".*"));

    	// true
    	System.out.println(s.isMatch("ab", ".*"));

    	// true
    	System.out.println(s.isMatch("aab", "c*a*b*"));
    }
}