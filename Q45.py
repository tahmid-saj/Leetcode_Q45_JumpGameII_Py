class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, 0, -1):
            j = i + nums[i-1] if i + nums[i-1] < len(nums) else len(nums)
            dp[i-1] = min(dp[i : j]) + 1 if i != j else 1001
        return dp[0]
