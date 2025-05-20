## LeetCode 3343. Count Number of Balanced Permutations
## �Ʀr���r��u�H�K�A���զX�v���X�X�� blanced (sum �_�Ʀ� == sum���Ʀ�) ����
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        @cache ## �Q�Ρu�禡�I�s�禡�v�Ӹ�
        def helper(d, odd, even, blance): ## �{�b�B�̼Ʀr d (�̧�9...0�B�z)
        ## �{�b�B�z�Ʀrd�A�_�ơB���Ʀ�u�U�ѴX��v�n��A�_�Ʀ�u�ٻݩ�h�֡v
            if odd == 0 and even == 0 and blance == 0:
                return 1    ## ��n�_�� (���) �Ƨ��A��n odd ��L���@�b�Χ��A�o��@�ո�
            if d<0 or odd<0 or even<0 or blance<0:  # ���@�ӥιL�Y (�ܭt)
                return 0    ## �������J���J�P�A�L�k��X��
            ans = 0
            dN = counter[d] ## �{�b�B�z�� digit d ���ƶq�� dN �ӡA���k���t
            for k in range(dN+1):   ## �� odd k �ӡA�� even (dN-k) ��
                now = helper(d-1, odd-k, even-(dN-k), blance-d*k)   ## �Ӧ����t�A���U��
                ans += comb(odd, k)*comb(even, dN-k)*now    ## �ƦC�զX: �D�_�Ʀ�B�D���Ʀ�
            return ans % 1000000007 ## �ƦC�զX�᪺�Ӥj�A�O�o���l�� 10^9+7

        nums = [int(c) for c in num]    ## ����u�r��v�ܦ��u�ƪ��}�C�v
        counter = Counter(nums) ## Hint 1 ��ĳ�Ƥ@�ơu�X�{�W�v�v
        total = sum(nums)   ## �C�@��ƥ[�_��
        if total%2 == 1: return 0   ## �u�[�_�ӡv�O�_�ơA�N�L�k�u�������t�v
        even = len(num) // 2    ## num �̡A���@�b�����Ʀ�� (�p���I�L����˥h)
        odd = len(num) - even   ## �ѤU���O�_�� ex. "123" �_�Ʀ즳 2 ��
        return helper(9, odd, even, total//2)   ## �q�Ʀr 9 �u�}�l��ơv
