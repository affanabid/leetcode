class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        res, pre, post = [0] * n, [0] * n, [0] * n
        pre[0], post[-1] = nums[0], nums[-1]
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i]

        for i in range(n):
            if i == 0:
                res[i] = post[i+1]
            elif i == n-1:
                res[i] = pre[i-1]
            else:
                res[i] = pre[i-1] * post[i+1]
        return res

nums = [1]

# nums = [-1,1,0,-3,3]

s = Solution()
print(s.productExceptSelf(nums))