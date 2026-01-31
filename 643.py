class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[0:k])
        res = curr / k
        l, r = 0, k
        while l < len(nums) and r < len(nums):
            curr = curr - nums[l] + nums[r]
            res = max(res, curr/k)
            l += 1
            r += 1
        return res
    
nums = [1,12,-5,-6,50,3]
s = Solution()
s.findMaxAverage(nums, 4)