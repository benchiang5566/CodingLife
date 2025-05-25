## LeetCode 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
## 要把陣列裡的 0 都變成正數，且希望 sum(nums1) == sum(sum2) 加總最小值

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        ## 把 nums 的總和 及 陣列有幾個 0 計算出來，因為以後者為基礎評估加總的需求
        sum1, zero1 = sum(nums1), nums1.count(0)
        sum2, zero2 = sum(nums2), nums2.count(0)
        ## 所有的 0 都加上 1，依此類推
        sum1 += zero1
        sum2 += zero2
        ## 判斷加總次數與需求，並回傳答案
        if sum1 == sum2 : return sum1
        ## 如有最大值出現，回傳最大值，前面無法滿足，就是無解
        if sum1 < sum2 and zero1>0 : return sum2
        if sum2 < sum1 and zero2>0 : return sum1
        return -1

