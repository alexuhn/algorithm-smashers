class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from functools import reduce
# 쪼개고 더하는 것은 알겠는데 쪼개고 정렬할 때 식별자들이랑 어떻게 원래대로 매칭시키지?
    
#         shit = []
#         ssibal = []
    
#        for i in range(len(logs)):
            
#             print(logs[i].split())
#             if logs[i].split()[1].isdigit():
#                 shit.append(logs[i].split()[1:])
                
#             else : 
#                 ssibal.append(logs[i].split()[1:])
#             print(shit, ssibal)
            
            # 람다를 알기 전 방식 풀지는 못 함
        
        strings = []
        digits = []
        
        for i in range(len(logs)):
            
            if logs[i].split()[1].isdigit():
                digits.append(logs[i])
            else : 
                strings.append(logs[i])
    
        strings.sort(key=lambda x: (x.split()[1:], x.split()[0]))  
        
        return strings + digits
    
    # 책에서 람다 사용법 읽고 푼 것
    # 이거 다 하는 데 2시간 정도 걸림
    # 리턴으로 리스트 합쳐지는 거 몰랐음