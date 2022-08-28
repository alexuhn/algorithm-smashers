class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = [log for log in logs if log.split()[1].isalpha()]
        digit_logs = [log for log in logs if log.split()[1].isdigit()]

        letter_logs = sorted(letter_logs, key=lambda x: (
            x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs

# 너무 어려우
# 문제 해석부터가 어려웠음
# 소트 람다 배움
# 레터로그 디짓로그 분리할 생각을 못 하고 식별자 제외 소트한 거에서
# 숫자랑 문자를 별도로 정렬할 방법을 찾느라 시간 너무 오래 걸림
