class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        globalmax = nums[0]

        i = 1
        while i < len(nums):
            n = nums[i]

            tempmax = max(n, n * currmax, n * currmin)
            tempmin = min(n, n * currmax, n * currmin)

            currmax = tempmax
            currmin = tempmin

            globalmax = max(globalmax, currmax)
            i += 1

        return globalmax