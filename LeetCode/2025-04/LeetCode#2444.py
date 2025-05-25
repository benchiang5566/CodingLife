## LeetCode 2444. Count Subarrays With Fixed Bounds
## �Ƥ@�ơu���X�� subarray�v ��n�� �̤p��minK....�̤j��maxK
## �i�Ρu����Ρv�ӨM�w�u�b�d�򤺡v�����׷���
## �� 3 �ا���:tailBad, tailHigh, tailLow �����u���ѡv�u��n�OmaxK�v�u��n�OminK�v
## ���� += tailBad...min(tailHigh, tailLow) �X�z�����ڪ��i��Ӽ�

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        ans = 0
        tailBad = tailHigh = tailLow = -1 ## �@�}�l���e�A���b���䪺����

        for head in range(len(nums)): ## ����Ρu�k�䪺�Y�v
            if nums[head] < minK or nums[head] > maxK: ## �W�L�d��
                tailBad = head ## �a��������
            if nums[head] == minK: ## ��n�O�uminK �̤p�ȡv
                tailLow = head ## �Хܡu��n�O minK �̤p�ȡv������
            if nums[head] == maxK: ## �Хܡu��n�O minK �̤p�ȡv������
                tailHigh = head ## ��n�O�umaxK �̤j�ȡv
            ## bad....high...llow....head
            ##    ^^^^ possible �i�઺�d��
            ## bad....high...llow....head
            ##    ^^^& possible �i�઺�d��
            possible = min(tailLow, tailHigh) - tailBad ## �Y�b head �ɡA���X�ئX�z�����ڦ�m
            if possible > 0: ans += possible ## �����O�u���ơv�~��[�J���פ�
        return ans
