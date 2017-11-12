/*
 * LeetCode: 8. String to Integer(atoi)
 * Finish Time: 2017.11.12 23:49
 * Time: 27min
 * Wrong Submissions: 4. For requirement corner case.
 * Tip: Integer.MAX_VALUE and Integer.MIN_VALUE
 */

class Solution8 {
    public int myAtoi(String str) {
        int ret = 0;
        int sign = 1;
        boolean start = false;
    	for (int i = 0; i < str.length(); i++) {
        	if (!start) {
        		char c = str.charAt(i);
        		if (c == ' ') {
        			continue;
        		} else if (c == '-') {
        			sign = -sign;
        			start = true;
        			continue;
        		} else if (c == '+' ) {
        			start = true;
        			continue;
        		} else if (c < '0' || c > '9'){
        			return 0;
        		} else {
        			start = true;
        		}
        	}
        	
        	char c = str.charAt(i);
        	if (c < '0' || c > '9') {
       			break;
       		}
           	int d = c - '0';
           	int temp = ret * 10 + d;
           	if (temp / 10 != ret) {
           		if (sign == 1) {
           			return sign * Integer.MAX_VALUE;
           		} else {
           			return sign * Integer.MIN_VALUE;
           		}
           	}
           	ret = ret * 10 + d;
        }
    	return ret * sign;
    }
    
    public static void main(String[] args) {
    	Solution8 s = new Solution8();
    	String input;
    	int output;

    	input = "-2147483648";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "+-2";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "a123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "-123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "-123aaaa";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "+123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "00123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "+00123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "-123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    	
    	input = "-00123";
    	output = s.myAtoi(input);
    	System.out.println(output);
    }
}