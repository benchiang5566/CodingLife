## LeetCode 3068. Find the Maximum Sum of Node Values
## �C���A�i�D�Y�� edge �A�� 2 �� node ���g�L XOR k �B��
## ���N�O�C���D 2 �ӡA�@�_ XOR �ݯ��@�h�� (tree ���c�@�I�������n)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0 ## ��u�[�`�v�����G
        min_diff = inf  ## �|�s��u�̤p�ܤƶq�vabs(num - (num^k))
        up = 0 ## ��@�X��
        for num in nums:    ## �C�ӼƦr�A�v�@����
            if num^k > num: ## �Y XOR ��u�ܤj�v�A�N XOR
                num = num^k ## �����ܤj
                up += 1 ##  ����@ 1 ��
            ans += num  ## �[�`�����G
            min_diff= min(min_diff, abs(num - (num^k))) ## �̤p���ܤƶq
        if up%2==0: return ans  ## �Y�O�u���ơv����@�A���ת������ӥ�
        else: return ans - min_diff ## �̤p���ܤƶq�u�n�����v�H����u���ơv����@
