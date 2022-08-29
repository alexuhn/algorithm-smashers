class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 단어는 case-insensitive하므로 계산 편의를 위해 미리 소문자로 변환
        paragraph = paragraph.lower()
        
        # 영문자와 공백을 제외한 나머지 기호를 공백으로 대치
        # 처음엔 빈 문자열로 대치했다가 "a,b,c"와 같은 경우에서 틀림
        paragraph = re.sub('[^a-zA-Z\s]', ' ', paragraph)
        
        words = paragraph.split()  # 단어 저장 리스트
        words_count = dict()  # 단어 등장 횟수 저장 딕셔너리

        most_common_count = 0  # 한 단어가 가장 많이 등장한 횟수
        most_common_word = ''  # 가장 많이 등장한 단어
        
        banned = set(banned)  # 빠른 탐색을 위해 리스트를 세트로 변환
        
        for word in words:
            if word in banned:  # 단어가 금지된 단어 세트 안에 있다면 무시
                continue
            
            if word in words_count:  # 단어가 딕셔너리에 기록된 적 있는 경우
                words_count[word] += 1  # 등장 횟수 갱신
                    
            else:  # 단어가 딕셔너리에 기록된 적 없는 경우 새로 기록
                words_count[word] = 1
                
            # 최대 등장 횟수를 넘는 경우 횟수와 단어 갱신
            if most_common_count < words_count[word]:
                most_common_count = words_count[word]
                most_common_word = word
                
        return most_common_word
                
