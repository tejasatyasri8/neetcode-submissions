class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def cs(idx, target, curr):
            if idx == len(candidates):
                if target == 0:
                    res.append(curr.copy())
                return

            # Pick
            if candidates[idx] <= target:
                curr.append(candidates[idx])
                cs(idx + 1, target - candidates[idx], curr)
                curr.pop()

            # Not Pick: skip duplicates
            i = idx + 1
            while i < len(candidates) and candidates[i] == candidates[idx]:
                i += 1

            cs(i, target, curr)

        cs(0, target, curr)
        return res