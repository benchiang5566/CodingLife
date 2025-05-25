## LeetCode 2094. Finding 3-Digit Even Numbers
## ㄏノ digits 皚柑计 0...9 舱 3 计案计逼
## 璝ノ for 癹伴ㄌ代氮皑ㄓ
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(list(map(str, digits)))   ## 计跑ダ计计
        ans = []    ##パ氮
        for i in range (100, 999, 2): ## р 3 计案计常刚筁
            cnt = Counter(list(str(i))) ## 计跑ダ计计
            if cnt<=counter: ans.append(i)  ## counter 计秖镑碞琌氮
        return ans
