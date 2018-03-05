/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode rh=new ListNode(0);
        rh.next=null;
        ListNode t=rh;
        int c=0;
        while(l1!=null || l2!=null){
            if(l1==null){
                ListNode n=new ListNode((l2.val+c)%10);
                n.next=null;
                c=(l2.val+c)/10;
                t.next=n;
                l2=l2.next;
            }else if(l2==null){
                ListNode n=new ListNode((l1.val+c)%10);
                n.next=null;
                c=(l1.val+c)/10;
                t.next=n;
                l1=l1.next;
            }else{
                ListNode n=new ListNode((l1.val+l2.val+c)%10);
                n.next=null;
                c=(l1.val+l2.val+c)/10;
                t.next=n;
                l1=l1.next;
                l2=l2.next;
            }
            t=t.next;
            System.out.println(t.val);
        }
        if(c>0){
            ListNode n=new ListNode(c);
            n.next=null;
            t.next=n;
        }
        return rh.next;
    }
}
