class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 투 포인터로 하는 방법을 생각해 보자
        세 수의 합이니까
        정렬을 먼저 한 다음,
        i, j, k 의 합이 0이 되는 경우
        i, j가 고정에 k를 돌리고
        i가 고정에 j를 한 칸 옮기고 k를 돌리고 하는 방법
        은 너무 오래 걸린다. """

        solution = []
        nums.sort()
        # 정렬함, i+1이 i랑 같은 경우 안 하고 넘어가는 방법 생각

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        solution.append([nums[i], nums[j], nums[k]])
        print(solution)
        return solution

        """아아니 왜 안됨?????
        오늘 중으로 개선해서 새로 업로드하겠음... 시간이 너무 없네..."""
