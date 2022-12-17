class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def find_two_sum_with_goal(nums, left, right, goal):
            answer = []
            while left < right:
                _sum = nums[left] + nums[right]
                if _sum == goal:
                    answer.append(sorted([goal, nums[left], nums[right]]))
                    right -= 1
                    left += 1
                elif _sum > goal:
                    right -= 1
                elif _sum < goal:
                    left += 1
            return answer

        # 1. PREPARE
        nums = sorted(nums)
        left, first_positive, right = 0, 0, len(nums) - 1
        for i, num in enumerate(nums):
            if num > -1:
                first_positive = i

        # 2. FIND
        # CASE A : use 0
        if nums[first_positive] == 0:
            result = find_two_sum_with_goal(nums, left, right, 0)
            if len(result) > 0:
                answer.append(result)

        # CASE B : no 0 usage
        left, right = 0, len(nums) - 1
        while nums[left] < 0:
            goal = nums[left] * -1

            l, r = first_positive, right
            result = find_two_sum_with_goal(nums, l, r, goal)
            if len(result) > 0:
                answer.append(result)

            left += 1

        while right < len(nums) and nums[right] > -1:
            goal = nums[right] * -1

            l, r = 0, first_positive - 1
            result = find_two_sum_with_goal(nums, l, r, goal)
            if len(result) > 0:
                answer.append(result)

            right += 1

        return list(answer)