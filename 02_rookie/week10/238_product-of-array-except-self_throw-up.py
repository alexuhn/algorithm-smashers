class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 책 안 보고 한 거 타임 리밋 뜸.
        from math import prod

        def zero(a):
            return 0
        answer = []
        if nums.count(0) > 1:
            return list(map(zero, nums))

        elif nums.count(0) == 1:
            ZIN = nums.index(0)
            nums.pop(ZIN)
            AP = prod(nums)
            BASE = list(map(zero, nums))
            BASE.insert(ZIN, AP)
            return BASE
            
        # 여기서 리밋 뜸
        elif nums.count(0) == 0:
            for i in range(len(nums)):
                answer.append(prod(nums)//nums[i])
            return answer

