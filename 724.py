from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rp, lp = [0] * (len(nums) + 2), [0] * (len(nums) + 2)
        for i in range(len(nums)):
            lp[i+1] = lp[i] + nums[i]

        for i in range(len(nums), 0, -1):
            rp[i] = rp[i+1] + nums[i-1]

        print(nums, '\n', lp, '\n', rp)
        for i in range(1, len(lp)-1):
            if lp[i-1] == rp[i+1]:
                return i-1
        return -1


nums = [1,7,3,6,5,6]
s = Solution()
print(s.pivotIndex(nums))