## LeetCode 1550. Three Consecutive Odds
## 判斷陣列裡面的，奇數個數，並回傳「True」or「False」
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0 ## 先設好裝奇數的空間
        for i in arr: ## 依序檢查陣列內的元素是否為奇
            if i%2==1:
                odd+=1
                if odd>=3: return True ## 達到標準，回傳 True
            else:
                odd = 0
        return False ## 反之 False

