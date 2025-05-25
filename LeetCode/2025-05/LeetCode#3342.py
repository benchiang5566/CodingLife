## LeetCode 3342. Find Minimum Time to Reach Last Room II
## 從 (0, 0) 出發，地下城的房間 (i, j) 在 moveTime[i][j] 才會開放
## 但「移動的時間」卻是 1 秒、2 秒、1 秒、2 秒....，這樣間隔，問最快何時到 (n-1, m-1)

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
       N, M = len(moveTime), len(moveTime[0])
       heap = []
       heappush(heap, (0, 0, 0,1)) ## 參數 1，對應「要花 1 秒走」，之後 3-s
       visited = set()
       visited.add((0, 0))  ## 起點，走過

       while heap:
        t, i, j, s = heappop(heap)
        if i==N-1 and j==M-1: return t ## 順利地走到終點的時間 t (理想狀況)

        for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):   ## 依序測試 4 個不同的方向
            if ii<0 or jj<0 or ii>=N or jj>=M: continue ## 超過範圍，不走
            if (ii, jj) in visited: continue    ## 走過，不走

            tt = max(t, moveTime[ii][jj])   ## 檢查房間開放了嗎? 要等到開放，才能走
            heappush(heap, (tt+s, ii, jj, 3-s)) ## 3-s 讓時間 1秒、2秒、1秒、2秒 間隔
            visited.add((ii, jj))   ## 走過
