import java.util.ArrayList;

/*
 * LeetCode: 7. Reverse Integer
 * Finish Time: 2017.11.12 23:15
 * Time: 5min
 * Wrong Submissions: 1, wrong position for return 0.
 * Tip: 1.Simplify the procedure. 2.Use tricky way to judge overflow.
 */

class Solution7 {
    public int reverse(int x) {
    	int reversed = 0;
    	while (x != 0) {
    		// Important.
    		int temp = reversed * 10 + x % 10;
    		if (temp / 10 != reversed) {
    			return 0;
    		}
    		reversed = temp;
    		x = x / 10;
    	}
    	return reversed;
    }
    
    public static void main(String[] args) {
    	Solution7 s = new Solution7();
    	
    	int input;
    	int output;
    	
    	// -2143847412
    	input = -2147483412;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// 0
    	input = 1534236469;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// 109
    	input = 901000;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// 321
    	input = 123;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// -321
    	input = -123;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	//21
    	input = 120;
    	output = s.reverse(input);
    	System.out.println(output);
    }
}

/*
 * LeetCode: 7. Reverse Integer
 * Finish Time: 2017.11.12 22:32
 * Time: 26min
 * Wrong Submissions: 2, one wrong iteration with ArrayList.remove(index), one exceed max int32;
 * Tip: 
 */

class Solution7Long {
    public int reverse(int x) {
        int sign = 1;
    	if (x < 0) {
    		sign = -1;
    		x = -x;
    	}
    	
    	ArrayList<Integer> xDigit = new ArrayList<Integer>();
    	while (x > 0) {
    		xDigit.add(x % 10);
    		x = x / 10;
    	}
    	
    	ArrayList<Integer> validDigit = new ArrayList<Integer>();
    	boolean found = false;
    	for (int i = 0; i < xDigit.size(); i++) {
    		if (found) {
    			validDigit.add(xDigit.get(i));
    		} else if (xDigit.get(i) == 0) {
    			continue;
    		} else {
    			found = true;
    			validDigit.add(xDigit.get(i));
    		}
    	}
    	
    	int out = 0;
    	long d = 1;
    	for (int i = validDigit.size() - 1; i >= 0; i--) {
    		if (Integer.MAX_VALUE - out < d * validDigit.get(i)) {
    			return 0;
    		}
    		out += validDigit.get(i) * d;
    		d = d * 10;
    	}
    	return out * sign;
    }
    
    public static void main(String[] args) {
    	Solution7Long s = new Solution7Long();
    	
    	int input;
    	int output;
    	
    	// 0
    	input = 1534236469;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// 109
    	input = 901000;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// 321
    	input = 123;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	// -321
    	input = -123;
    	output = s.reverse(input);
    	System.out.println(output);
    	
    	//21
    	input = 120;
    	output = s.reverse(input);
    	System.out.println(output);
    }
}