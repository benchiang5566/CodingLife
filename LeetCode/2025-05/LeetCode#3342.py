## LeetCode 3342. Find Minimum Time to Reach Last Room II
## �q (0, 0) �X�o�A�a�U�����ж� (i, j) �b moveTime[i][j] �~�|�}��
## ���u���ʪ��ɶ��v�o�O 1 ��B2 ��B1 ��B2 ��....�A�o�˶��j�A�ݳ̧֦�ɨ� (n-1, m-1)

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
       N, M = len(moveTime), len(moveTime[0])
       heap = []
       heappush(heap, (0, 0, 0,1)) ## �Ѽ� 1�A�����u�n�� 1 ���v�A���� 3-s
       visited = set()
       visited.add((0, 0))  ## �_�I�A���L

       while heap:
        t, i, j, s = heappop(heap)
        if i==N-1 and j==M-1: return t ## ���Q�a������I���ɶ� t (�z�Q���p)

        for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):   ## �̧Ǵ��� 4 �Ӥ��P����V
            if ii<0 or jj<0 or ii>=N or jj>=M: continue ## �W�L�d��A����
            if (ii, jj) in visited: continue    ## ���L�A����

            tt = max(t, moveTime[ii][jj])   ## �ˬd�ж��}��F��? �n����}��A�~�ਫ
            heappush(heap, (tt+s, ii, jj, 3-s)) ## 3-s ���ɶ� 1��B2��B1��B2�� ���j
            visited.add((ii, jj))   ## ���L
