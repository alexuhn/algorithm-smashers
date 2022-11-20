class Solution:
    def trap(self, height: List[int]) -> int:
        rain = height[:]
        top = max(height)
        l_top_pos = height.index(top)
        r_top_pos = len(height) - 1 - height[::-1].index(top)

        #fill in left side
        cur = 0
        for i in range(0, l_top_pos):
            if cur < height[i]: cur = height[i]
            rain[i] = cur

        #fill in center side
        rain[l_top_pos:r_top_pos+1] = [top] * (r_top_pos + 1 - l_top_pos)
        
        #fill in right side
        cur = 0
        for i in reversed(range(r_top_pos, len(height))):
            if cur < height[i]: cur = height[i]
            rain[i] = cur

        return sum([rain[i] - height[i] for i in range(len(height))])