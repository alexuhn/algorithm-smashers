import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # 소문자 변환

        pattern = re.compile("[a-z0-9]")  # alphanumeric 문자 패턴
        s = pattern.findall(s)  # alphanumeric 문자만 도출

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True
