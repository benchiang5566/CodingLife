## LeetCode 1931. Painting a Grid With Three Different Colors
## �� 3 �ئ�m�� mxn �� grid �ۦ�A�۾F����P��A�u���X�صۦ�k�v

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7   ## �Ψӭp��u�l�ơv
        ## m <= 5���A�i�� bitmask �Хܡu���� 5 �檺��m�v�A�C��0,1,2,3 �@ 4 ����� 2 bit
        @cache  ## �ݰ_�ӴN�� DP �����D�A�Ρu�禡�I�s�禡�v�ӸѡA�b����k�v�@�u���S���L�h�v
        def checkCol(prev, j):  ## ����O prev �ϮסA�{�b�u����col j�v�A���׬O�h��
            return checkIJ(0, j, prev, 0)   ## �� helper2() �䵪�סA�ðO�U����
        ## �W���� cache �i��֤j�q�p��C�U���٦b�s�P�p�⤤�A���ϥ� @cache ���O�Х\��
        def checkIJ(i, j, prev, now): ## �{�b�B�z�� (i, j) �o��A�W���U�B�����k��
            if i==m: return checkCol(now, j+1)  ## �� bitmask prev bitwise ��X�u�����v���u��m�N�X�v
            if j==n: return 1   ## �̤W�����ơA���������A�o�� 1 �ӸѡA�� 1 ��
            left = prev >> (i*2) & 3    ## �� bitmask now bitwise ��X�u�����v���u��m�N�X�v
            if i==0: up = 0 ## �̤W�����ơA�S�� up ����l
            else: up = (now >> (i-1)*2) & 3 ## �� bitmask now bitwise ��X�u�W����v�u��m�N�X�v
            ans = 0
            for c in range(1,4):    ## �{�b�Q�񪺥i��u��m�N�X 1, 2, 3�v���չL�@�� (�쥻�S�񪺥N�X�O 0)
                if c != left and c != up:   ## �P�u����v�u�W���v�����ۦP�A�N�i�u�禡�I�s�禡�v�A�`�J��s
                    ans += checkIJ(i+1, j, prev, now + (c<<(i*2)))  # ��J c ��X�s�� bitmask
                    ans %= MOD  ## �ȼƦr�Ӥj�A�n�p��u�l�ơv
            return ans
        return checkCol(0, 0)   ## �W��U�B����k�A�̧ǧ䵪��
