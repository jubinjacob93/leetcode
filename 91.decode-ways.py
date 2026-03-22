#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        dp=[0]*(n+1)  
        dp[n]=1
        for i in range(n-1, -1, -1):
            if s[i]!='0':
                dp[i]+=dp[i+1] 
            if i+1<n and 10<=int(s[i:i+2])<=26:
                dp[i]+=dp[i+2] 
        return dp[0]
        
# @lc code=end

