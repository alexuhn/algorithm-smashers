class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 1차시도
        # digit_logs = [log for log in logs if log.split()[-1].isdigit()]
        # letter_logs = [log for log in logs if not log.split()[-1].isdigit()]
        # return sorted(letter_logs, key=lambda log: itemgetter(log.split()[1:], log.split()[0])) + digit_logs
        
        #2차시도
        # def cmp_func(log_pair):
        #     # index, log = log_pair 이걸 포기하고 아랫줄로 쓰면 시간이 왕 빨라짐
        #     index, log = log_pair[0], log_pair[1]
        #     if log.split()[-1].isdigit():
        #         return (1, index)
        #     else:
        #         return (-1, log.split()[1:], log.split()[0])
        # return [log[1] for log in sorted(enumerate(logs), key=cmp_func)]
        
        # 3차시도
        return [log[1] for log in sorted(enumerate(logs), key= lambda pair: (1, pair[0]) if pair[1].split()[-1].isdigit() else (-1, pair[1].split()[1:], pair[1].split()[0]))]
        
        # 제일 표 많이 받은 풀이 - 졸라 개느림ㅋ
        # digits = []
        # letters = []
        # for log in logs:
        #     if log.split()[1].isdigit():
        #         digits.append(log)
        #     else:
        #         letters.append(log)
        
        # letters.sort(key = lambda x: x.split()[0])
        # letters.sort(key = lambda x: x.split()[1:])
        # result = letters + digits
        # return result

# # 참고한 링크
# 정렬 함수 공식 문서 : https://docs.python.org/ko/3/howto/sorting.html
# 숫자인지 판별하는 함수들의 차이 : https://it-neicebee.tistory.com/33
# 정렬함수 내의 람다에서 어떻게 인덱스를 받을까? : https://stackoverflow.com/questions/5432762/getting-index-of-item-while-processing-a-list-using-map-in-python
