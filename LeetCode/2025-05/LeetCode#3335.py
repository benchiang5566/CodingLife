## LeetCode 3335. Total Characters in String After Transformations I
## transform 1 ���A�r���|���k 1 ��(a �� b, b��c, ...,z��ab) �� t ����,�ܴX�Ӧr��
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9+7   ## �]�� t �ܤj�A�n���l��
        @cache  ## �Q�Ρu�禡�I�s�禡�v�ѳo���D��
        def helper(t): ## ��֡u�禡�I�s�禡�v�����ѼƼƶq�A�ܦ��u�r�� 'a'�v�g�L t ���ഫ�L��A�ܦ��X�Ӧr��
            if t< 26: return 1 ## �r�� 'a' �b 25 �����A���٬O 1 �Ӧr��
            return (helper(t-26)+helper(t-26+1)) % MOD
            ## �α� 26 ���A�ܦr�� 'a'+ �Ψ� 26 ���A�ܦr�� 'b' �b��ɤ@�� 1 ���A�ܦr�� 'a'
        ans = 0
        for c in s:
            diff = ord(c) - ord('a') ## �n��ɤ@�� diff ���A�|�ܦr�� 'a'
            ans += helper(t+diff) ## �r�� 'a' �ഫ t+diff ��
        return ans % MOD
