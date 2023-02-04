/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = prices[0];
    let result = 0;

    prices.forEach(price => {
        if (price < minPrice) {
            minPrice = price;
            return;
        }
        if (result < price - minPrice) {
            result = price - minPrice;
        }
    })

    return result;
};
