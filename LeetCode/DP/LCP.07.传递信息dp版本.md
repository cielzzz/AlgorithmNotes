## 解题思路

**此题用DFS、DP都可以解决，这里放DP解法**

求方案数，最优值，用DP

edge in relation，拿出来的edge比如为[0,2],[2,1],[3,4] ，而每个组的src是edge[0] dst是edge[1]



## 代码

```
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int: 
        #[src,dst]表示source，也就是start,dst表示destination，即end
        #dp[i][j]表示经过i轮传递到编号为j的方案个数
        dp = [[0] * (n+1) for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(k):
            for edge in relation: #每个edge比如[0,2]，源src是edge[0]，终点dst是edge[1]
                src = edge[0]
                dst = edge[1]
                dp[i+1][dst] += dp[i][src]
        return dp[k][n-1]
```




