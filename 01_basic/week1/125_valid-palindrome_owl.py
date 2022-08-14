class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        
        if s == s[::-1] :
            return "true"


# 4번 line -> filter에 스트링을 넣어도 리스트 반환해서 join 필수
# 7번 line -> ''.join 없으면 더 빠르고 메모리도 적게 먹음, 처음엔 리스트로 이용해서 ''.join사용해서 제춣했었음.