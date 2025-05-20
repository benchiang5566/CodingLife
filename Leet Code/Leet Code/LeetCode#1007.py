## LeetCode 1007. Minimum Domino Rotations For Equal Row
## �C�Ӱ��P���W�U����I�ơC�@��ӱư��ơA�D 1 �Ǳ����A���@��C (tops �� bottoms) ���ۦP
## �p�G��F�����ȡA��ܡu�W�B�U�v�@�w�|���@�ӬO�u�@�P�v���ơA����X�ӡA�K��ΰj��ѥX�ӵ���
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)   ## N �Ӱ��P
        counter = Counter(tops) + Counter(bottoms)  ## �Ƥ@�U�u�X�{���ơv
        k, v = counter.most_common(1)[0]    ## �X�{�̦h�I�ƬO k�A�X�{���� v

        if v < N: return -1 ## �p�G�X�{���ơu�����v�A�@�w���ѡAreturn -1

        ans1 = ans2 = 0 ## ����إi��: ��W��(���� ans1)�B��U��(���� ans2)
        for i in range(N):  ## �C�Ӱ��P���@���A�ؼСu�� k ����W���h or �U���z
            if k == tops[i] and k != bottoms[i]: ans2 += 1 ## �W���Ok�A���U�����Ok�A���N�n�u��1���v���U���঳k
            if k == bottoms[i] and k != tops[i]: ans1 += 1  ## �U���Ok�A���W�����Ok�A���N�n�u��1���v���W���঳k
            if k != tops[i] and k != bottoms[i]: return -1  ## �Y�W�U�����O K ���N�^�ǥ��ѡC
        return min(ans1, ans2)  ## ��W��?��U��? �Τp������ !
