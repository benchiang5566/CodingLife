## LeetCode 1550. Three Consecutive Odds
## �P�_�}�C�̭����A�_�ƭӼơA�æ^�ǡuTrue�vor�uFalse�v
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0 ## ���]�n�˩_�ƪ��Ŷ�
        for i in arr: ## �̧��ˬd�}�C���������O�_���_
            if i%2==1:
                odd+=1
                if odd>=3: return True ## �F��зǡA�^�� True
            else:
                odd = 0
        return False ## �Ϥ� False

