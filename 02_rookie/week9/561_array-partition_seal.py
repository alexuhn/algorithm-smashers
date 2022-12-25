class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([v for i, v in enumerate(sorted(nums)) if i % 2 == 0])