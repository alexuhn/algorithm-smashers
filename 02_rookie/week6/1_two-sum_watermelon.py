class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 결과로 index를 반환해야 하므로 index 값을 함께 저장
        nums = [(index, value) for index, value in enumerate(nums)]
        
        # value를 기준으로 정렬
        nums.sort(key=lambda num: num[1])
        
        # 투 포인터로 탐색
        left, right = 0, len(nums) - 1
        while left < right:
            result = nums[left][1] + nums[right][1]
            if result < target:
                # 수가 부족한 경우 left를 늘려 더 큰 수를 가져옴
                left += 1
                
            elif target < result:
                # 수가 넘치는 경우 right을 줄여 더 작은 수를 가져옴
                right -= 1
            
            else:
                # target과 일치하는 경우
                return [nums[left][0], nums[right][0]]
            
