// Solution 1
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort((x, y) => x - y)
    let result = 0;
    for (let i = 0; i < nums.length; i += 2) {
        result += nums[i]
    }
    return result;
};


// Solution 2
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    return nums.sort((x, y) => x - y).reduce((accumulator, currentValue, index) => index % 2 ? accumulator : accumulator + currentValue, 0);
};
