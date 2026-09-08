class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stk = []

        for i in range(len(cost)):

            if len(stk) < 2:
                stk.append(cost[i])
            
            else:
                o1 = stk[-1]
                o2 = stk[-2]
                stk.append(cost[i] + min(o1,o2))


        return min(stk[-1],stk[-2])

        