class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()

        result = 0
        for i in range(1, len(nums)+1):
            if i % 2 != 0:
                continue
            else:
                result += nums[-i]

        return result
