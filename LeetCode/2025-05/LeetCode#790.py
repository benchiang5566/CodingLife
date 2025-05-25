## LeetCode 790. Domino and Tromino Tiling
## ����اΪ������P�A�ǲ� 1x2 �� L�� �����P�A�� 2xn ���X�إi��ƪk

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def helper(n):
            if n==0: return 1
            if n==1: return 1
            if n==2: return 2
            ## �� 1 �ӡA�i�H����A�i�H���
            ans = helper(n-1) + helper(n-2)
            ## �]�i�H�� L�� ����k�� (�����L��)�A �|�����u������L���v
            for i in range(3, n+1, 2):  ## �u������L���v���b����
                ans = (ans + helper(n-i) * 2) % MOD ## �����L��
                ## �]�i�H�Ρu���L����ﱵ�v���Φ�
            for i in range(4, n+1, 2):
                ans = (ans + helper(n-i) * 2) % MOD
            return ans % MOD
        return helper(n)
