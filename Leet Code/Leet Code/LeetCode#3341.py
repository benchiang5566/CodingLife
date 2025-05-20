## LwwtCode 3341. Find Minimum Time to Reach Last Room I
## n x m �a�U���̡A���ǩж�(��l)�@�}�l����i�J�A�n���� moveTime[i][j] �����ɶ���A�~��i�J
## �аݳֳ̧̧֡A�O�n�h�[�~��i�J�u�̫᪺�ж�(n-1, m-1)�v

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        N, M = len(moveTime), len(moveTime[0])  ## �����D�a�Ϫ����B�e

        heap = []   ## �i�Q�� priority queue �Ӹѳo�D
        heappush(heap, (0, 0, 0))   ## �@�}�l�b�� 0 ��A�ݦb 0, 0 ���ж�
        visited = set() ## ���L���ж��A�N���ΦA��
        visited.add((0, 0)) ## �����L (0, 0) �o�өж�

        while heap: ## ����i�����
            t, i, j = heappop(heap) ## �{�b�̧֪��ɶ��b�o��
            if i == N-1 and j == M-1: return t  ## �̧֪��t�סA���̫� 1 ��(���I)

            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):   ## �� 4 �Ӥ�V��
                if ii<0 or jj<0 or ii>=N or jj>=M: continue ## �W�L��ɪ��A����
                if (ii, jj) in visited: continue    ## ���L���A����
                ## �N�i�b�Y�Ӯɶ�(���U�@�Ӯɶ��I)�A���L ii, jj �o��
                heappush(heap, (max(t, moveTime[ii][jj])+1, ii, jj))
                visited.add((ii, jj))   ## �o��i�J heap �N����A���i��
