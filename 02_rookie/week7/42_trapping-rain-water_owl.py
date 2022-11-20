class Solution:
    def trap(self, height: List[int]) -> int:
        """
        새로운 접근
        높이가 제일 큰 것을 찾음
        높이가 제일 큰 것이 2개 미만(1개) 일때 1을 감소
        다시 높이가 제일 큰 것을 찾음
        높이가 제일 큰 것이 2개 이상일 때
        높이가 제일 큰 것들의 사이(거리)를 1씩만 계산(그 층의 물만 파악) 예를 들면 1, 4, 5, 7번째 네 개가 있다 하면
        4-1-1, 5-4-1, 7-5-1을 구함 => 이 층에는 물이 2, 0, 1 만큼 있음 => 3만큼 있음
        다시 높이를 1씩 감소
        높이가 제일 큰 것이 많아 질 때, 다시 요소요소의 사이거리를 계산(그 층만 파악)
        높이가 1이 되는 경우까지 계산 후 종료
        """
        # max_h : 리스트의 가장 높은 값 / water : 물의 양(for문 돌면서 더해질 예정)

        # for index, value in enumerate(height):

        max_h = max(height)
        water = 0
        while max_h > 0:
            # print("추적중 max_h 현재", max_h, "진행중")
            if height.count(max_h) < 2:
                # print("1번", height)
                height[height.index(max_h)] = max_h - 1
                max_h -= 1
                # print("2번", height)
            else:
                # print("else로 넘어옴")
                max_index = list(
                    filter(lambda x: height[x] == max_h, range(len(height))))
                # print("max_index뽑기", max_index)
                for i in range(len(max_index) - 1):
                    # print("i=", i)
                    water += max_index[i+1] - max_index[i] - 1
                    height[max_index[i]] = max_h - 1
                height[max_index[i+1]] = max_h - 1
                max_h -= 1
                # print("else임", water, max_h)
            # print("height 어떻게 됐나?", height)
        return water

        """
        근데 이 개 비효율적인 방법인데 해보고 싶어서 그냥 해봄
        풀리긴 하는데 시간에 걸림
        """
