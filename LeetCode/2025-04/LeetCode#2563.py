## LeetCode 2563. Count the Number of Fair Pairs
## 若 Lower <= nums[i] + nums[j] <= upper 叫  fair pair，總共有幾組?
## 直覺用 2 層 for 迴圈，但 nums 有 15^5 太大，不能用 2 層迴圈。
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() ## Hint 1 建議 sort() 因 sort 後的結過一樣多
        ## 再來就簡單了， 用 for 迴圈，決定右邊界，再 binary search 看左邊的範圍
        ans = 0
        for i in range(1, len(nums)):
            ## 修改 binary search 的參數，不要用 nims[:i] 即加速
            j_left = bisect_left(nums, lower - nums[i], hi = i)
            j_right = bisect_right(nums, upper - nums[i], hi = i)
            ans += j_right - j_left
        return ans
