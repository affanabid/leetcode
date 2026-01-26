class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        zero = 0
        while zero < n and nums[zero] != 0:
            zero += 1
        nonzero = zero 
        while nonzero < n and nums[nonzero] == 0:
            nonzero += 1
        while zero < n and nonzero < n:
            if nums[nonzero] == 0:
                nonzero += 1
            elif nums[zero] != 0:
                nonzero += 1
            else:
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                zero += 1
                nonzero += 1
        return nums                