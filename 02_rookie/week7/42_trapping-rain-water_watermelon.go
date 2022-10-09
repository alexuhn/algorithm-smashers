func trap(height []int) int {
    result := 0
    left, right := 0, len(height) - 1
    leftMax, rightMax := height[left], height[right]
    
    for left < right {
        if height[left] <= rightMax {
            result += leftMax - height[left]
            left++
            if leftMax < height[left] {
                leftMax = height[left]
            }
        } else if height[right] <= leftMax {
            result += rightMax - height[right]
            right--
            if rightMax < height[right] {
                rightMax = height[right]
            }
        }
    }
    
    return result
}
