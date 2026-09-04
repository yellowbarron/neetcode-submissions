class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curcomb,total):
            if total == target:
                res.append(curcomb.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            curcomb.append(candidates[i])
            dfs(i+1,curcomb,total+candidates[i])

            curcomb.pop()
            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            dfs(i+1,curcomb,total)

        dfs(0,[],0)

        return res

