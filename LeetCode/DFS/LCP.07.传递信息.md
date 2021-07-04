## 解题思路

**此题用DFS、DP都可以解决，这里放DFS解法**
暴力搜索问题，用DFS（走到死胡同再返回）

DFS 从节点0开始做深度优先搜索，每一步记录当前所在节点以及经过的轮数，当经过K轮，如果位于节点n-1，则res+1


## 代码

```
#建立有向边条件
graph = collections.defaultdict(set)
for x,y in relation:
    graph[x].add(y) #x可以理解为start,y可以理解为end
```
```
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        #建立有向边条件
        graph = collections.defaultdict(set)
        for x,y in relation:
            graph[x].add(y) #x可以理解为start,y可以理解为end

        def dfs(x,step):
            if step == k:
                if x == n-1:
                    self.res += 1
                return 
            for y in graph[x]: #此时y从graph中找下一个传递的人
                dfs(y, step + 1)
        self.res = 0
        dfs(0,0)
        return self.res
```




