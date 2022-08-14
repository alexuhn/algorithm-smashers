class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s))
        s = s.lower()

        if s == s[::-1]:
            return True


# 4번 line -> filter에 스트링을 넣어도 리스트 반환해서 join 필수
# 7번 line -> ''.join 없으면 더 빠르고 메모리도 적게 먹음, 처음엔 리스트로 이용해서 ''.join사용해서 제춣했었음.
# 8번 line -> True값을 결과로 리턴하는 거를 잘 몰라서 첨엔 print("true")를 이용했는데
# 오류 나서 return "true"로 submit함. 근데 됨. 나중에 문제 발견해서 True로 수정.
