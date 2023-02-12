class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """ 생각할 것
        1. 계속 작아지기만 하는 경우(어떤 숫자도 그 다음 숫자보다 작지 않은 경우) 리턴 0
        2. 최소값 기준 우측에 최대값 위치 시 그 차를 리턴
        3. 최소값 기준 좌측에 최대값 위치 시
            - 


        흠. 최소 포인터 최대 포인터를 min, max로 놓고
        동시에 우측으로 이동시키면서 더 작은 수를 만날때마다 min을 치환하고
        max는 더 큰 수를 만날때마다 치환한 다음
        max - min?
        그리고 max - min 값이 0이거나 음수인 경우 리턴은 0

        """

        if len(prices) < 2:
            return 0
        
        elif len(prices) == 2 and prices[1] - prices[0] <= 0:
            return 0

        elif len(prices) == 2 and prices[1] - prices[0] > 0:
            return prices[1] - prices[0]


        else:
        
            mini = prices[0]
            maxi = prices[1]
            
            for i in range(0,len(prices)-1):
                if mini > prices[i]:
                    mini = prices[i]
                if maxi < prices[i+1]:
                    maxi = prices[i+1]
                print(mini,maxi)
            if maxi - mini > 0 and maxi != prices[1]:
                return maxi - mini

            elif maxi - mini <= 0:
                return 0

            elif maxi == prices[1] and prices[0] > prices[1]:
                return 0

            else:
                return maxi - mini