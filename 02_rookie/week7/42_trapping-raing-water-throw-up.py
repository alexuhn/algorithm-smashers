class Solution:
    def trap(self, height: List[int]) -> int:

    
        rain_water = 0
        left, right = 0, len(height)-1
        left_zzang, right_zzang = height[left], height[right]
        
        while left < right:
            left_zzang = max(height[left], left_zzang)
            right_zzang = max(height[right], right_zzang)
            if left_zzang <= right_zzang:
                rain_water += left_zzang - height[left]
                left += 1
            else:
                rain_water += right_zzang - height[right]
                right -= 1
        return rain_water
                        
