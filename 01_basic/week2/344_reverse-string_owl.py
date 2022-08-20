class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]
#         슬라이싱으로 원소를 교체해줌

# 첨에 든 생각은 s = s[::-1] 로, s를 s[::-1]로 할당하는 것이었는데, 지난 주에 이야기 했던 깊은-얕은 문제로
# 인하여 작동하지 않음.
# s 자체에 할당하는 것이 불가하므로 s의 원소를 교체하는 것이 유효한지 확인해 봄.
# s[:]는 곧 s의 원소의 나열이고, s[::-1]와 길이는 같고 순서만 반대임.
# s의 원소 각각에 대하여 s원소의 역순인 원소들을 교체하는 것이 유효.
