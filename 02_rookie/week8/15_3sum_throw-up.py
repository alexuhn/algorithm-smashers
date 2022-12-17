class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 저번 때처럼 투 포인트로 해야겠구나 해도 리스트가 정렬 돼 있지 않으면 어케하라는 건지 싶다가도 아웃풋에서 원래 놈 구할 필요 없이 그냥 값을 구하고 때려 맞히기만 한 거라는 걸 깨달음

        answer = []
        nums.sort()
        for i in range(len(nums)-2):
            L = i+1
            R = len(nums)-1  
            if i > 0 and nums[i] == nums[i-1]: # 중복출력 방지 [[-1,-1,2],[-1,0,1],[-1,0,1]]
                continue           
            while L < R:
                if nums[L] + nums[R] + nums[i] < 0:
                    L += 1
                elif nums[L] + nums[R] + nums[i] > 0:
                    R -= 1
                else:
                    answer.append((nums[i], nums[L], nums[R]))
                    while L < R and nums[L] == nums[L+1]:     # 이 새끼들도 i 처럼 땡겨줘야겠음
                            L += 1
                    while L < R and nums[R] == nums[R-1]:
                            R -= 1
                    L += 1
                    R -= 1      # Input [-2,0,0,2,2] Output [[-2,0,2],[-2,0,2]] 중복 또 뜸 > line19
        return answer