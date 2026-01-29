class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        mx = -(float(inf))
        while l < r:
            curr = min(height[l], height[r]) * (r-l)
            mx = max(mx, curr)
            if height[l+1] > height[r-1]:
                l += 1
            else:
                r -= 1
        return mx