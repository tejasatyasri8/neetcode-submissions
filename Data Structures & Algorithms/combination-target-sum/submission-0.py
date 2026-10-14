class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def cs(start, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                cs(i, remaining - nums[i])
                curr.pop()

        cs(0, target)
        return res
        