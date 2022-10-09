/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let volume = 0;
    const stack = []; // 변곡점 기록
    
    for (let x = 0; x < height.length; x++) {
        while (stack && height[stack.at(-1)] < height[x]) {
            const last_x = stack.pop();
            
            if (!stack.length) {
                // 좌측에 빗방울을 막아줄 벽이 없는 경우
                break;
            }
            
            const water = Math.min(height[x], height[stack.at(-1)]) - height[last_x];
            
            // 양 쪽 벽 사이 거리만큼 빗방울을 채움
            volume += water * (x - stack.at(-1) - 1);
        }
        stack.push(x);
    }
    
    return volume;
};
