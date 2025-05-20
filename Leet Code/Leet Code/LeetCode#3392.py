## LeetCode 3392. Count Subarrays of Length Three With a Condition
## 數一數「有多少 subarry」長度為3、且前後加起來 == 中間 /2

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0 ## 迴圈前面 ans 是 0
        for i in range (len(nums)-2): ## 逐一處理
            if(nums[i] + nums[i+2]) * 2 == nums[i+1]:
                ans += 1 ## 迴圈裡，符合條件的 ｢答案｣  +1
        ## 迴圈後，把答案送出去
        return ans
