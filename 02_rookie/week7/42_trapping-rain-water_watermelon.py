class Solution:
    def trap(self, height: List[int]) -> int:
        def started_from_top(height_map):
            """
            가장 높은 높이의 땅이 최좌측에 있는 맵에서 물방울을 세는 함수
            """
            result = 0 # 모은 빗방울
            
            # 높이에 대하여 내림차순으로 땅을 저장 [(높이, 위치)]
            stack = [(height_map[0], 0)]

            for index, height in enumerate(height_map[1:]):
                while stack and stack[-1][0] <= height:
                    # 더 높은 땅을 만난 경우 낮은 땅을 스택에서 제거
                    last_height, last_index = stack.pop()
                    
                    # 높은 땅과 낮은 땅의 차이만큼 물방을 추가
                    result += (height - last_height) * (index - last_index)
                    
                    # 현재 높이를 가진 땅의 위치를 제거된 땅의 위치로 이동
                    index = last_index
                    
                stack.append((height, index)) # 새로운 땅을 추가
                
            return result
        
        max_index = height.index(max(height)) # 가장 높은 높이의 땅 위치
        
        # 가장 높은 높이의 땅을 기준으로 좌우를 분리하여,
        # 우측 땅은 started_from_top 실행, 좌측 땅은 좌우를 반전하여 started_from_top 실행
        return started_from_top(height[0: max_index + 1][::-1]) + started_from_top(height[max_index:])
    
