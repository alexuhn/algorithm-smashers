class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target에서 nums[i] 뺀 값이 nums 안에 존재 하는지 판별

        import numpy
        # 중복되는 원소들의 인덱스 모두 찾기 기능 (numpy.where 메소드)

        for i in range(len(nums)):
            if target - nums[i] in nums and target != nums[i]*2:
                return i, nums.index(target - nums[i])
            elif target - nums[i] in nums and nums.count(nums[i]) > 1:
                # count메소드로 같은 요소가 둘 이상일 때를 조건으로 함
                nums = numpy.array(nums)
                # 주어진 list를 array로 변환
                return numpy.where(nums == nums[i])[0]
                # numpy.where(nums == x)[0]  =>  주어진 배열에서 x라는 요소가 있는 위치를 모두 반환

                # 책 안 보고 해서 배열이나 딕셔너리 못 쓰겠어서 안 함... 커밋하고 책 읽을 것.
                # 그래서 효율 똥망 제출은 되는데 짱 느림.
