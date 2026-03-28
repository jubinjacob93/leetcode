#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        
         # Early exit if n is 1 or 2 
        if n  == 1 or n  == 2:
            return n
        
        #Initializing one and two as ways(1) and ways(2) respectively
        one, two=1,2
        
        # Since the number of ways matches the fibonaccis sequence i.e. ways(n)=ways(n-1)+ways(n-2)
        # Solution is also space optimized as we just need to keep track of previous two values
        for i in range(3, n+1):
            temp=two
            two=one+two 
            one=temp

        return two

        
# @lc code=end


