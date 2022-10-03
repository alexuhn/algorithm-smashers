class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            if (target - nums[i]) in nums[i+1:]:
                pair =  nums.index(target - nums[i], i + 1)
                return [i, pair]
                # 풀기는 했지만 마음에 들지는 않았다. 그 이유는
                # in 으로 1회 순회하고, index로 또 순회하기 때문이다.

 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    # 개 오래걸림. in이나 index가 최적화 되어 있는 듯