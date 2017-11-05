package linkedlist;
import java.util.ArrayList;

public class LinkedList {
	public ListNode arrayToLinkedList(int[] a) {
		ListNode dummy = new ListNode(0);
		ListNode head = dummy;
		for (int i = 0; i < a.length; i++) {
			ListNode node = new ListNode(a[i]);
			head.next = node;
			head = head.next;
		}
		return dummy.next;
	}
	
	public void printLinkedList(ListNode node) {
		ArrayList<String> a = new ArrayList<String>();
		while (node != null) {
			a.add(String.valueOf(node.val));
			node = node.next;
		}
		
		System.out.println(String.join(",", a));
	}
}