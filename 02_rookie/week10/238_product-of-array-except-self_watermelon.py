class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # from_left: 첫 인덱스부터 시작하여 i번 인덱스까지 곱한 값을 저장하는 리스트
        # from_right: i번 인덱스부터 시작하며 마지막 인덱스까지 곱한 값을 저장하는 리스트
        from_left, from_right = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]

        # 뒤의 for문에서 에러가 나지 않도록 첫 번째 값과 마지막 값을 미리 설정
        from_left[0], from_right[-1] = nums[0], nums[-1]

        # from_left와 from_right 리스트를 채워나감
        size = len(nums)
        for i in range(1, size):
            from_left[i] = from_left[i - 1] * nums[i]
            from_right[size - 1 - i] = from_right[size - i] * nums[size - 1 - i]

        # for문에서 에러가 나지 않도록 첫 번째 값과 마지막 값은 따로 처리
        result = [from_right[1]]
        for i in range(1, size - 1):
            result += [from_left[i - 1] * from_right[i + 1]]
        result += [from_left[-2]]

        return result
