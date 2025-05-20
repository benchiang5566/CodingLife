## LeetCode 3335. Total Characters in String After Transformations I
## transform 1 次，字母會往右 1 格(a 變 b, b變c, ...,z變ab) 問 t 次後,變幾個字母
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9+7   ## 因為 t 很大，要取餘數
        @cache  ## 利用「函式呼叫函式」解這個題目
        def helper(t): ## 減少「函式呼叫函式」內的參數數量，變成「字母 'a'」經過 t 次轉換過後，變成幾個字母
            if t< 26: return 1 ## 字母 'a' 在 25 之內，都還是 1 個字母
            return (helper(t-26)+helper(t-26+1)) % MOD
            ## 用掉 26 次，變字母 'a'+ 用到 26 次，變字母 'b' 在抬升一次 1 次，變字母 'a'
        ans = 0
        for c in s:
            diff = ord(c) - ord('a') ## 要抬升一次 diff 次，會變字母 'a'
            ans += helper(t+diff) ## 字母 'a' 轉換 t+diff 次
        return ans % MOD
