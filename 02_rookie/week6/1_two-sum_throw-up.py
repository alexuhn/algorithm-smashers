class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     if abs(nums[i]) <= abs(target):
        #         left = abs(target) - abs(nums[i])
        #         if left in nums[i+1:]:
        #             index = nums.index(left,i+1)
        #             output.extend([i,index])
        # return output
    # 음수를 절대값으로 풀어보려 했지만
    # 리스트에 -2, 2 이따구로 들어가면 인덱스 번호 특정 못 한다는 걸 깨달음 다른 방법으로 풀어야 함...
    # 타겟 10 주고 13, -3 주면 부등호에서 13이 걸러진다는 것도 깨달음 
        
        output = []
        for ind, num in enumerate(nums):                                                # enumerate 배움
                left = target - num
                if left in nums[ind+1:]:
                    output.extend([nums.index(num), nums[ind+1:].index(left)+ind+1])    # 거른 부분 앞에서 리스트 따로 구축하고 따오면 되는거였음
                    
                    return output 
                
    # 분명 딕셔너리로 풀 수 있을 거 같은데 딕셔너리에서 인덱스 번호 어케 부를지 막막해서 시도 안함
                