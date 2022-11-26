class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # three sum 문제 => 하나의 target + two sum 문제
        # 아래에서 two sum을 찾을 때 투 포인터를 이용하기 위해 nums를 정렬
        nums.sort()
        
        # 중복되는 triplet을 제거하기 위해 최종 결과를 set으로 저장
        result_set = set()
        
        # 가장 작은 숫자와 가장 큰 숫자는 target이 될 수 없으므로 제외
        for index in range(1, len(nums) - 1):
            # two sum의 목표
            target = nums[index]        
            
            # 투 포인터
            left, right = 0, len(nums) - 1
            
            # 좌측 포인터와 우측 포인터가 target에 닿으면 종료
            while left < index and index < right:
                two_sum = nums[left] + nums[right]
                if two_sum < target * -1:
                    left += 1
                elif target * -1 < two_sum:
                    right -= 1
                else:
                    # target을 만든 경우 이를 기록
                    result_set.add((nums[left], target, nums[right]))
                    
                    # 무한 반복을 돌지 않도록 임의의 포인터를 이동
                    left += 1
    
        # 튜플로 구성된 set을 출력 형태에 맞게 리스트로 변경
        return list(result_set)
