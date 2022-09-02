class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter
        import operator
        
        # list1 = re.sub(r'[\W_]+', ' ', paragraph) # 영숫자가 아닌 문자를 비워버리는 코드를 따옴
                                                  # 근데 ''를 ' '으로 바꾸면 공란이 생길 줄 알았는데 안 생기더라 왜지...
                                                  # 일단 풀려서 쭉 해봄   
#         
#         list1 = list1.lower().split()
#         list1 = [x for x in list1 if x != 'hit']
#         list1 = Counter(list1)
        
#         answer = dict(sorted(list1.items(), key=operator.itemgetter(1), reverse = True))

#         return next(iter(answer))  예제 안 읽고 풀어서 폭망함...


        list1 = re.sub(r'[\W_]+', ' ', paragraph)
        list1 = list1.lower().split() # 소문자로 다 바꾸고 간격을 기준으로 나눔
        list1 = [x for x in list1 if x not in banned] # banned 배열 안에 있는 걸 제외하고 한 리스트에 합침
        list1 = Counter(list1) # 리스트 안에 있는 요소들을 counter 함수로 셈
        answer = dict(sorted(list1.items(), key=operator.itemgetter(1), reverse = True)) # 갯수를 기준으로 역순정렬 후 딕셔너리로 바꿈
        return next(iter(answer)) # 딕셔너리 첫 항을 리턴함
