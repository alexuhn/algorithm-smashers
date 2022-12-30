/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const result = [1];

    for (i = 1; i < nums.length; i++) {
        result.push(result[result.length - 1] * nums[i - 1]);
    }

    let power = nums[nums.length - 1];
    for (i = nums.length - 2; -1 < i; i--) {
        result[i] *= power;
        power *= nums[i];
    }

    return result;
};
