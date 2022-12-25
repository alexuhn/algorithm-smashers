class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 배열 오름차순으로 정렬하고 홀수번째만 다 더하면 그게 최대 아닐까

        nums.sort()
        result = 0 

        for i in range(len(nums)):
            if i % 2 == 0:
                result += nums[i]

        return result
