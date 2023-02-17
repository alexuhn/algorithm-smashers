# ===== Solution 1 =====
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        entire_list = [] # 연결 리스트의 모든 값을 저장할 리스트
        while head:
            entire_list.append(head.val)
            head = head.next

        return entire_list == entire_list[::-1]

# ===== Solution 2 =====
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True

        slow = head
        fast = head
        reverse = None
        
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while slow:
            if slow.val != reverse.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True
