## LeetCode 3337. Total Characters in String After Transformations II
## 將 s[i] 變成「接下來」nums[s[i]-'a'] 個字母('z'之後會回到'a')字母可能會越來越多
## 要做 t<=10^9 次，讓這題「不能真的用迴圈模擬器」，是「超級難的題目」
## 把繁複的運算，累計在 26x26的矩陣裡，變成「矩陣乘法」
## 統計 s 的字母出現次數 freq*(M 的 t 次方) 再 (把每個字母的數目) 逐項加起來
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
