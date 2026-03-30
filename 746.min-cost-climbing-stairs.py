#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        # total_cost is the cost of using that stair as a stepping stair to the next one
        total_cost=[0]*(n)
        total_cost[0] = cost[0]
        total_cost[1] = cost[1]

        # Here we break down total_cost as the cost of the current stair plus min of the total_cost of (n-1) or (n-2) stair
        for j in range(2,n):
            total_cost[j]=cost[j]+min(total_cost[j-1], total_cost[j-2])

        # Return the total cost to get to the top (index n) stair, however we don't need to add cost[n+1] (although non-existent) here because it is not being used as a stepping stair
        return min(total_cost[n-2], total_cost[n-1])
        
    
        
# @lc code=end

