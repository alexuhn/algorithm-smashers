class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxpa = s[0]

        if s == s[::-1] or len(s) < 2:
            return s

        for i in range(len(s) - 1):
            if i + 2 < len(s) and s[i] == s[i + 2]:
                l, r = i - 1, i + 3
                while l > -1 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                maxpa = max([maxpa, s[l+1:r]], key=len)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = i - 1, i + 2
                while l > -1 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                maxpa = max([maxpa, s[l+1:r]], key=len)
        return maxpa

# 테스트 케이스 150개 중에 148번에 걸려서 안 됨...
