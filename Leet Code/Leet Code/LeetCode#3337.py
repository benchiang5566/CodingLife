## LeetCode 3337. Total Characters in String After Transformations II
## �N s[i] �ܦ��u���U�ӡvnums[s[i]-'a'] �Ӧr��('z'����|�^��'a')�r���i��|�V�ӶV�h
## �n�� t<=10^9 ���A���o�D�u����u���ΰj��������v�A�O�u�W�������D�ءv
## ���c�ƪ��B��A�֭p�b 26x26���x�}�̡A�ܦ��u�x�}���k�v
## �έp s ���r���X�{���� freq*(M �� t ����) �A (��C�Ӧr�����ƥ�) �v���[�_��
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        def mat_pow(Mat, t):
            if t==1: return Mat
            half = mat_pow(Mat, t//2)
            ans = mat_mult(half, half)
            if t%2==1: ans = mat_mult(ans, Mat)
            return ans

        MOD = 10**9+7
        def mat_mult(Mat1, Mat2):
            I, K, J = len(Mat1), len(Mat2), len(Mat2[0])
            ans = [[0] * J for i in range(I)]
            for i in range(I):
                for j in range(J):
                    for k in range(K):
                        ans[i][j] += Mat1[i][k] * Mat2[k][j]
                    ans[i][j] %= MOD
            return ans

        M = [[0] * 26 for i in range(26)]
        for i in range(26):
            for j in range(i+1, i+nums[i]+1):
                M[i][j%26] = 1
        counter = Counter([ord(c) - ord('a') for c in s])
        freq = [[counter[i] for i in range(26)]]
        ans = mat_mult(freq, mat_pow(M, t))
        return sum(ans[0]) % MOD
