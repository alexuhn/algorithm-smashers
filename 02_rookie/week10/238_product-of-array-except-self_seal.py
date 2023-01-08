class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1, nums[0]]
        i = 2
        while i < len(nums):
            result.append(nums[i-1] * result[-1])
            i += 1

        i -= 1 # 마지막 요소로
        prod = nums[i] # 마지막 요소 넣기

        i -= 1 # 마지막에서 2번째 요소로
        while i >= 0:
            result[i] *= prod
            prod *= nums[i]
            i -= 1

        return result