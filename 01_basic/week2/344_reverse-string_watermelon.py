class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # 좌측 끝과 우측 끝을 차례대로 swap
        for index in range(len(s) // 2):
            s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
