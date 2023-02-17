# ===== Solution 1 (792 ms) =====
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

    
# ===== Solution 2 (665 ms) =====
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

    
# ===== Solution 3 (674 ms) =====
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
            fast = fast.next.next       # fast 이동
            prev_reverse = reverse      # reverse 저장
            next_slow = slow.next       # slow.next 저장
            reverse = slow              # reverse 변경
            reverse.next = prev_reverse # reverse를 역으로 연결
            slow = next_slow            # slow 이동

        if fast:
            slow = slow.next

        while slow:
            if slow.val != reverse.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True
