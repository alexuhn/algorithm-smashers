class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 무식한 방법 당연히 시간초과
        # profit = []
        # for bf in range(len(prices)):
        #     for af in range(bf+1,len(prices)):
        #         if prices[bf] < prices[af]:
        #             profit.append(prices[af]-prices[bf])
        # 왜 ruturn max(profit) 하면 빈 리스트라 뜨고 에러가 남?
        # print(profit) 하니까 [1, 1, 1, 1, 5, 3, 3] 랑 [] 출력 됨 뭐지 썅...
        # 아니 max 함수에 default = 0 넣어줘야 5가 반환 됨? 애초에 빈 리스트가 아닌데
        # return max(profit, default = 0)
        
        # 좀 빨라졌지만 이것도 느림 개시이부래 max 함수 빅오가 n이라서 포문 안에 쓰면 개느린가 봄
        # 중첩되는 요소에서 인덱스 번호 뽑으면 제일 앞에 있는 놈 번호로 리턴 됨 그거 노리고 함
        profit = []
        if prices.index(min(prices)) < prices.index(max(prices)):
            return max(prices) - min(prices)
        else:
            for bf in range(len(prices)):
                profit2 = max(prices[bf+1:], default = 0) 
                if prices[bf] < profit2 :
                    profit.append(profit2 - prices[bf])
            return max(profit, default = 0)
        
        # 책에서 sys 함수를 배워왔다 하지만 이건 개같다 그러니 안 쓸거임
        # 근데 이거 왜 에러 뜨지 None 뜬다 카는데 다 int형인데 왜 비교가 안됨
        # '<' not supported between instances of 'int' and 'NoneType'
        # max_prices = max(prices)
        # min_prices = min(prices)
        # print(type(max_prices))
        # print(type(prices.index(max_prices)))
        # print(prices.index(max_prices))
        # if prices.index(max_prices) > prices.index(min_prices):
        #     return max_prices - min_prices

        # 진폭이 큰 새끼를 찾는거니까 최대값 전으로 슬라이스해서 최소값 찾고
        # 최소값 후로 슬라이스해서 최대값 찾은 후 거기서 차이가 큰 새끼 리턴해볼까 함
        # 근데 최소나 최대가 중첩되는 게 많아서 max나 min으로 다 고려하지 못 한다면? 개썅...
