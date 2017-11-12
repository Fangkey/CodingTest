/*
 * LeetCode: 9. Palindrome Number
 * Finish Time: 2017.11.13 00:38
 * Time: 5min
 * Wrong Submissions: 0.
 * Tip: Using reversed integer.
 */

class Solution9 {
    public boolean isPalindrome(int x) {
    	if (x < 0) {
    		return false;
    	}
    	
    	// Important. reversed integer
        int reversed = 0;
        int temp = x;
        while (temp != 0) {
        	reversed = reversed * 10 + temp % 10;
        	temp /= 10;
        }
    	
    	return reversed == x;
    }
    
    public static void main(String[] args) {
    	Solution9 s = new Solution9();
    	
    	int input;
    	boolean ret;
    	
    	// true
    	input = 9999;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 1000000001;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// false
    	input = -1;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 0;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 12321;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// false
    	input = -12321;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	//false
    	input = 12345;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    }
}

/*
 * LeetCode: 9. Palindrome Number
 * Finish Time: 2017.11.13 00:16
 * Time: 21min
 * Wrong Submissions: 3. wrong d
 * Tip:
 */

class Solution9Long {
    public boolean isPalindrome(int x) {
    	if (x < 0) {
    		return false;
    	}
    	
    	// Important d from 0.1
        double d = 0.1;
        int len = 0;
        int temp = x;
    	while (temp != 0) {
    		temp /= 10;
    		d *= 10;
    		len += 1;
    	}
    	
    	int dd = (int) d;
    	
    	int t1 = x;
    	int t2 = x;
    	for (int i = 0; i < len / 2; i++) {
    		if (t1 / dd != t2 % 10) {
    			return false;
    		}
    		t1 = t1 - t1 / dd * dd;
    		dd /= 10;
    		t2 /= 10;
    	}
    	
    	return true;
    }
    
    public static void main(String[] args) {
    	Solution9Long s = new Solution9Long();
    	
    	int input;
    	boolean ret;
    	
    	// true
    	input = 9999;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 1000000001;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// false
    	input = -1;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 0;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// true
    	input = 12321;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	// false
    	input = -12321;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    	
    	//false
    	input = 12345;
    	ret = s.isPalindrome(input);
    	System.out.println(ret);
    }
}