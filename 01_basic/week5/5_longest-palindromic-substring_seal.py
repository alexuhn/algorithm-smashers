# 오늘 푼거, 예전에 다른애가 푼거 참고함
class Solution:
    def longestPalindrome(self, s: str) -> str:
      def get_nearest_pal(s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
          left, right = left - 1, right + 1
        return s[left+1:right]

      max_pal = ''
      center = int(len(s) / 2)
      distance = 1
      direction = -1
      
      while center > -1 and center < len(s):
        pal = get_nearest_pal(s, center, center)
        max_pal = max([max_pal, pal], key=len)

        if center < len(s) - 1:
          pal = get_nearest_pal(s, center, center + 1)
          max_pal = max([max_pal, pal], key=len)
      
        center += distance * direction
        distance += 1
        direction *= -1

      return max_pal

# 제일 빠르게 통과하는 코드
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        max_length = 1
        start = 0
        for i in range(1, len(s)):
            one_more_letter_word = s[i-max_length:i+1]
            two_more_letter_word = s[i-max_length-1:i+1]
            
            if self.isPalindrome(two_more_letter_word) and i-max_length-1 >= 0:
                start = i - max_length - 1
                max_length += 2
            elif self.isPalindrome(one_more_letter_word):
                start = i - max_length
                max_length += 1
        return s[start:start+max_length]

# 옛날에 통과했던건데 이제는 통과안함
class Solution:
    #팔린드롬의 부분도 팔린드롬이다.
    def longestPalindrome(self, s: str) -> str:
        original = s
        s = s.lower()
        candidate = s[0]
        
        l = 0
        r = len(s) - 1
        length = len(s)
        
        while length > 0:
            if (l == 0 and s[l:r+1] == s[r::-1]) or (s[l:r+1] == s[r:l-1:-1]): # is Palindrome substring
                return original[l:r+1]
            else:
                l += 1
                r += 1
                if r == len(s):
                    length -= 1
                    l, r = 0, length - 1