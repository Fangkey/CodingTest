import linkedlist.ListNode;
import linkedlist.LinkedList;

/*
 * LeetCode: 2. Add Two Numbers
 * Finish Time: 2017.11.05 23:37
 * Time: 43min, include ListNode, LinkedList
 * Wrong Submissions: 0
 */
class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        int inc = 0;
        while (l1 != null && l2 != null) {
        	int v = l1.val + l2.val + inc;
        	inc = v / 10;
        	ListNode node = new ListNode(v % 10);
        	head.next = node;
        	head = head.next;
        	l1 = l1.next;
        	l2 = l2.next;
        }
        
        if (l1 != null) {
        	while (l1 != null) {
        		int v = l1.val + inc;
        		inc = v / 10;
        		ListNode node = new ListNode(v % 10);
        		head.next = node;
        		head = head.next;
        		l1 = l1.next;
        	}
        }
        
        if (l2 != null) {
        	while (l2 != null) {
        		int v = l2.val + inc;
        		inc = v / 10;
        		ListNode node = new ListNode(v % 10);
        		head.next = node;
        		head = head.next;
        		l2 = l2.next;
        	}
        }
        
        if (inc == 1) {
        	ListNode node = new ListNode(1);
        	head.next = node;
        }
        
        return dummy.next;
    }
    
    public static void main(String[] args) {
    	Solution2 s = new Solution2();
    	LinkedList linkedList = new LinkedList();
    	
    	int[] a1 = {1, 2, 3};
    	int[] a2 = {7, 8, 9};
    	
    	ListNode l1 = linkedList.arrayToLinkedList(a1);
    	ListNode l2 = linkedList.arrayToLinkedList(a2);
    	
    	ListNode r = s.addTwoNumbers(l1, l2);
    	linkedList.printLinkedList(r);
    }
}