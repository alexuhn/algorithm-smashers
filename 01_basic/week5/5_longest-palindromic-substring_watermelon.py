# 첫 번째 풀이(runtime 534 ms)
def longestPalindrome(self, s: str) -> str:
    max_length, result = 1, s[0]  # 최장 길이와 해당 단어

    # 홀수 길이를 갖는 palindrome
    for middle in range(len(s)):
        left, right = middle - 1, middle + 1
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # 이 시점에서 left와 right는 palindrome 단어 바깥을 가리킴
        if max_length < right - left - 1:
            max_length = right - left - 1
            result = s[left + 1: right]

    # 짝수 길이를 갖는 palindrome
    for middle in range(len(s) - 1):
        if s[middle] != s[middle + 1]:  # 두 글자가 같지 않은 경우 무시
            continue

        left, right = middle - 1, middle + 2
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # 이 시점에서 left와 right는 palindrome 단어 바깥을 가리킴
        if max_length < right - left - 1:
            max_length = right - left - 1
            result = s[left + 1: right]

    return result
     
    
# 두 번째 풀이(runtime 246 ms)
def longestPalindrome(self, s: str) -> str:
    result = s[0]  # 최장 palindrome

    for middle in range(len(s)):            
        # 홀수 길이 palindrome의 경우: max_length < 2 * dx + 1
        dx = (len(result) - 1) // 2 + 1
        while (0 <= middle - dx and middle + dx < len(s) and 
               s[middle - dx: middle + dx + 1] == s[middle - dx: middle + dx + 1][::-1]):
            result = s[middle - dx: middle + dx + 1]
            dx += 1

        # 짝수 길이 palindrome의 경우: max_length < 2 * dx + 1 + 1
        dx = (len(result) - 2) // 2 + 1
        while (0 <= middle - dx and middle + dx + 1 < len(s) and 
               s[middle - dx: middle + dx + 2] == s[middle - dx: middle + dx + 2][::-1]):
            result = s[middle - dx: middle + dx + 2]
            dx += 1

    return result
    
    
# indentation 참고: https://peps.python.org/pep-0008/#indentation
