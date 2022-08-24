class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []  # Letter-log와 Digit-log를 따로 저장할 리스트
        
        for log in logs:
            # log의 맨 마지막 문자를 통해 Letter-log인지 Digit-log인지 검사
            if log[-1].isnumeric():  # str.isnumeric() => str이 numeric 문자인지 검사
                digit_logs.append(log)
            else:
                # Letter-log의 경우 이후 사전순 정렬을 위해 각 단어를 분리해 저장
                letter_logs.append(log.split())
        
        # 정렬은 안정적임이 보장된다. 즉, 여러 레코드가 같은 키를 가질 때, 원래의 순서가 유지된다.
        # Letter-log가 같을 경우 identifier로 정렬될 수 있도록 미리 identifier로 정렬
        letter_logs.sort()
        
        # identifier를 제외한 단어를 기준으로 사전순 정렬
        letter_logs.sort(key=lambda letter_log: letter_log[1:])
        
        # Letter-log를 다시 올바른 출력 형식으로 변환
        letter_logs = [" ".join(letter_log) for letter_log in letter_logs]
        
        return letter_logs + digit_logs
