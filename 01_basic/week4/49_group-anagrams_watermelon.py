class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}  # 단어를 사전순 정렬한 값을 키, 원본 단어를 값으로 갖는 딕셔너리
        
        for string in strs:
            key = "".join(sorted(string))  # 단어를 사전순 정렬한 키
            
            # 키가 딕셔너리에 존재하는 경우 원본 단어를 값으로 추가
            if key in group:  
                group[key].append(string)
            
            # 키가 딕셔너리에 존재하지 않는 경우 새로운 키 설정
            else:
                group[key] = [string]
        
        return [value for value in group.values()]
