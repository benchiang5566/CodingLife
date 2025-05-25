## LeetCode 1922. Count Good Numbers
## n ������ơA�ŦX�u���Ʀ�񰸼ơB�_�Ʀ���ơv���X��?
## �i�Q�Ρu�禡�I�s�禡�v���Ĳv��X�u���Ʀ�5�إi��B�_�Ʀ�4�إi��v���`��

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7   ##�]�̦h10^15 �� 1000 ����ƫܤj�A�ҥH�n���uMOD���l�ơv
        @cache ##�Q�Ρu�禡�I�s�禡�v�C���u���@�b�v�b���_�ӡA�t�X cache �ܧ�

        def helper(n, start):   ## n��ƮɡA�}�l��� start �|���� 4+start �إi��
            if n==0: return 1 ## �פ����:������ 0 ��ơA�n���W�Ҧ���
            if n==1: return 4+start ## ���ơA�|�^��5�B�_�ơA�|�^��4
            n2 = n//2 ## �u���@�b�v�����
            ans = helper(n2, start) ## ��ƩI�s��ơA�u���b�v���}�l�A�P�쥻�}�l
            if n%2==1: ans = ans * (4+start) %MOD ## �̫�ѤU����ơA���� 4 or 5

            if n2%2==0:ans = ans * helper(n2, start) % MOD ##�禡�I�s�禡
            else : ans = ans * helper(n2, 1-start)% MOD ##�禡�I�s�禡
            return ans
        return helper(n, True) ##start ��, True ���� 4+1 �B False����4+0
