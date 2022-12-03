/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b)
    const result = []
    
    for (i = 0; i < nums.length - 2; i++) {
        // 중복인 경우 넘어간다.
        if (0 < i && nums[i - 1] === nums[i]) {
            continue;
        }
        
        let left = i + 1, right = nums.length - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            
            if (sum < 0) {
                // 현재 left 숫자와 중복인 숫자 전부 넘어가기
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                left++;
            } else if (0 < sum) {
                // 현재 right 숫자와 중복인 숫자 전부 넘어가기
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }
                right--;
            } else {
                result.push([nums[i], nums[left], nums[right]]);
                
                // 현재 left 숫자와 중복인 숫자 전부 넘어가기
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                left++;
                
                // 현재 right 숫자와 중복인 숫자 전부 넘어가기
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }
                right--;    
            }
        }
    }
    
    return result;
};
