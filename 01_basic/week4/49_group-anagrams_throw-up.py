class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          # from collections import Counter

        # list1 = []
        # for i in strs:
        #     list1.append(''.join(sorted(list(i))))

        # dict1 = dict(Counter(list1)).keys()  # 사전 정렬로 모든 문자 조합을 하나로 귀결 -> 비교할 수 있는 기초 문자열

        # list3 = []

        # for dictcnt in range(len(list(dict1))): # 기초 문자열과 반복문으로 비교
        #     list2 = [] # 리스트를 매번 초기화 해서 변수를 하나만 사용
        #     for strscnt in range(len(strs)): # 주어지는 문자열 하나하나 일일이 비교

        #         if ''.join(sorted(list(strs[strscnt]))) == list(dict1)[dictcnt]: # 비교하려는 문자가 기초 문자열에 속해 있으면

        #             list2.append(strs[strscnt]) # 리스트에 문자 구성이 똑같은 문자열을 추가
        #     list3.append(list2)

        # return list3  

        # 시간 초과로 폭망함
        
        standard = {}
        for word in strs:
            if ''.join(sorted(word)) not in standard:
                standard[''.join(sorted(word))] = []
                standard[''.join(sorted(word))].append(word)
            elif ''.join(sorted(word)) in standard:
                standard[''.join(sorted(word))].append(word)
                
            #     standard[''.join(sorted(word))] =+ word 이런 식이 안되는 이유를 모르겠다 key를 일단 선언해야 되는건가
        return list(standard.values())