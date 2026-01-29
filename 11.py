class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height)-1
        mx = -(float('inf'))
        while l < r:
            curr = min(height[l], height[r]) * (r-l)
            mx = max(mx, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mx

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
s.maxArea(height)