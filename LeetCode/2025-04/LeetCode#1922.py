## LeetCode 1922. Count Good Numbers
## n い计才案计案计计借计Τ碭?
## ノㄧΑ㊣ㄧΑΤ瞯т案计5贺计4贺羆计

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7   ##程10^15  1000 计┮璶MOD緇计
        @cache ##ノㄧΑ㊣ㄧΑ–Ωち癬ㄓ皌 cache 跑е

        def helper(n, start):   ## n计秨﹍计 start 穦癸莱 4+start 贺
            if n==0: return 1 ## 沧ゎ兵ン:ち跑 0 计璶┮Τ计
            if n==1: return 4+start ## 案计穦肚5计穦肚4
            n2 = n//2 ## ち计
            ans = helper(n2, start) ## ㄧ计㊣ㄧ计オ秨﹍籔セ秨﹍
            if n%2==1: ans = ans * (4+start) %MOD ## 程逞计癸莱 4 or 5

            if n2%2==0:ans = ans * helper(n2, start) % MOD ##ㄧΑ㊣ㄧΑ
            else : ans = ans * helper(n2, 1-start)% MOD ##ㄧΑ㊣ㄧΑ
            return ans
        return helper(n, True) ##start , True 癸莱 4+1  False癸莱4+0
