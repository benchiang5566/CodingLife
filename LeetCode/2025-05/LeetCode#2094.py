## LeetCode 2094. Finding 3-Digit Even Numbers
## �ϥ� digits �}�C�̪��Ʀr 0...9 �A�եX 3 ��ư��ơA�b�u�p��j�v�Ƨ�
## �Y�� for �j��u�̧Ǵ��v�A���װ��W�X��
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(list(map(str, digits)))   ## �Ʀr�ܦr���A�b�Ƥ@��
        ans = []    ##�u�Ѥp��j�v�񵪮�
        for i in range (100, 999, 2): ## �� 3 ��ư��Ƴ��չL
            cnt = Counter(list(str(i))) ## �Ʀr�ܦr���A�b�Ƥ@��
            if cnt<=counter: ans.append(i)  ## counter �ƶq���A�N�O����
        return ans
