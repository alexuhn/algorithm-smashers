class Solution:
    def isPalindrome(self, s: str) -> bool:
        core = [c for c in s.lower() if c.isalnum()]
        return core == core[::-1]