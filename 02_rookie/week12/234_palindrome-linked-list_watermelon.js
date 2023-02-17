/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let fast = head;
    let slow = head;
    let reverse = null;

    while (fast && fast.next) {
        fast = fast.next.next;
        prev_reverse = reverse // reverse 저장
        next_slow = slow.next // slow.next 저장
        reverse = slow;
        reverse.next = prev_reverse;
        slow = next_slow;
    }

    if (fast) {
        slow = slow.next;
    }

    while (slow && slow.val === reverse.val) {
        slow = slow.next;
        reverse = reverse.next;
    }
    return !slow;
};
