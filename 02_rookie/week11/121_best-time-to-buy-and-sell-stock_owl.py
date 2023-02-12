 mini = prices[0]
        maxi = prices[1]

        for i in range(0,len(prices)-1):
            if mini > prices[i]:
                mini = prices[i]
            if maxi < prices[i+1]:
                maxi = prices[i+1]
            # print(mini,maxi)
        if maxi - mini > 0 and maxi != prices[1]:
            return maxi - mini
        elif maxi - mini <= 0 or maxi == prices[1]:
            return 0