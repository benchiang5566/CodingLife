## LeetCode 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
## �n��}�C�̪� 0 ���ܦ����ơA�B�Ʊ� sum(nums1) == sum(sum2) �[�`�̤p��

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        ## �� nums ���`�M �� �}�C���X�� 0 �p��X�ӡA�]���H��̬���¦�����[�`���ݨD
        sum1, zero1 = sum(nums1), nums1.count(0)
        sum2, zero2 = sum(nums2), nums2.count(0)
        ## �Ҧ��� 0 ���[�W 1�A�̦�����
        sum1 += zero1
        sum2 += zero2
        ## �P�_�[�`���ƻP�ݨD�A�æ^�ǵ���
        if sum1 == sum2 : return sum1
        ## �p���̤j�ȥX�{�A�^�ǳ̤j�ȡA�e���L�k�����A�N�O�L��
        if sum1 < sum2 and zero1>0 : return sum2
        if sum2 < sum1 and zero2>0 : return sum1
        return -1

