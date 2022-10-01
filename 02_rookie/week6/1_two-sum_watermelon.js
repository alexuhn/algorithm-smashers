/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // 한 번 검사한 숫자에 대하여 숫자-인덱스 쌍을 저장할 객체
    const checked = {};
    
    for (const [index, num] of nums.entries()) {
        if (target - num in checked) {
            return [index, checked[target - num]];
        }
        checked[num] = index;
    }
};
