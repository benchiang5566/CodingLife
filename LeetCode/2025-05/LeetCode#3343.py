## LeetCode 3343. Count Number of Balanced Permutations
## 计﹃繦獽舱搓碭 blanced (sum 计 == sum案计) 计
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        @cache ## ノㄧΑ㊣ㄧΑㄓ秆
        def helper(d, odd, even, blance): ## 瞷矪柑计 d (ㄌ9...0矪瞶)
        ## 瞷矪瞶计d计案计逞碭璶恶计临惠ぶ
            if odd == 0 and even == 0 and blance == 0:
                return 1    ## 案 (计) 逼Ч odd рノЧ眔舱秆
            if d<0 or odd<0 or even<0 or blance<0:  # ヴノ筁繷 (跑璽)
                return 0    ## ぃ┋ǐ璊礚猭搓秆
            ans = 0
            dN = counter[d] ## 瞷矪瞶 digit d 计秖Τ dN オだ皌
            for k in range(dN+1):   ## 倒 odd k 倒 even (dN-k) 
                now = helper(d-1, odd-k, even-(dN-k), blance-d*k)   ## 酚だ皌┕暗
                ans += comb(odd, k)*comb(even, dN-k)*now    ## 逼舱: 珼计珼案计
            return ans % 1000000007 ## 逼舱び癘眔緇计 10^9+7

        nums = [int(c) for c in num]    ## р﹃跑Θ计皚
        counter = Counter(nums) ## Hint 1 某计计瞷繵瞯
        total = sum(nums)   ## –计癬ㄓ
        if total%2 == 1: return 0   ## 癬ㄓ琌计碞礚猭キАだ皌
        even = len(num) // 2    ## num 柑Τ案计计 (计翴礚兵ン彼)
        odd = len(num) - even   ## 逞琌计 ex. "123" 计Τ 2 
        return helper(9, odd, even, total//2)   ## 眖计 9 秨﹍计
