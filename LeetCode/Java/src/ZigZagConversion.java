/*
 * LeetCode: 5. LongestPalindromicSubstring
 * Finish Time: 2017.11.12 00:30
 * Time: 36min
 * Wrong Submissions: 4
 */

class Solution6 {
    public String convert(String s, int numRows) {
    	if (numRows == 1) {
    		return s;
    	}
    	
        String ret = "";
    	for (int i = 0; i < numRows; i++) {
        	if (i == 0 || i == numRows - 1) {
        		int index = i;
        		while (index < s.length()) {
        			ret += s.substring(index, index + 1);
        			index += numRows * 2 - 2;
        		}
        	} else {
        		int index1 = i;
        		// Important. Init start
        		int index2 = i + (numRows - i - 1) * 2;
        		while (index1 < s.length() || index2 < s.length()) {
        			if (index1 < s.length()) {
        				ret += s.substring(index1, index1 + 1);
            			index1 += numRows * 2 - 2;
        			}
        			if (index2 < s.length()) {
        				ret += s.substring(index2, index2 + 1);
        				// Important. Same step
            			index2 += numRows * 2 - 2;
        			}
        		}
        	}
        }
        return ret;
    }
    
    public static void main(String[] args) {
    	Solution6 s = new Solution6();
    	
    	String input;
    	int row;
    	String output;
    	
    	// AEBDFC
    	input = "ABCDEF";
    	row = 3;
    	output = s.convert(input, row);
    	System.out.println(output);
    	
    	// ABDC
    	input = "ABCD";
    	row = 3;
    	output = s.convert(input, row);
    	System.out.println(output);
    	
    	// AB
    	input = "AB";
    	row = 3;
    	output = s.convert(input, row);
    	System.out.println(output);
    	
    	// A
    	input = "A";
    	row = 1;
    	output = s.convert(input, row);
    	System.out.println(output);
    	
    	// PAHNAPLSIIGYIR
    	input = "PAYPALISHIRING";
    	row = 3;
    	output = s.convert(input, row);
    	System.out.println(output);
    }
}