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

# 제일 빠르다는거 같이보려고 가져옴
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Idea: Go one way and cast shadows. Then go the other way.
        Runtime O(n)
        """

        tallest = height[0]
        area = 0
        tallest_index = 0
        running_area = 0
        for i in range(1, len(height)):
            curr = height[i]
            if curr >= tallest:
                tallest = curr
                area += running_area
                tallest_index = i
                running_area = 0
            else:
                running_area += tallest - curr

        tallest = height[-1]
        running_area = 0
        for i in range(len(height) - 1, tallest_index - 1, -1):
            curr = height[i]
            if curr >= tallest:
                tallest = curr
                area += running_area
                running_area = 0
            else:
                running_area += tallest - curr
        return area
