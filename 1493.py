class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r, z = 0, 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                z += 1
                if z > 1:
                    res = max(res, r-l-1)
                    while z > 1:
                        if nums[l] == 0:
                            z -= 1
                        l += 1
            r += 1
        return max(res, r-l-1)
                    


                
            