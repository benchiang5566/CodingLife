class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        s = set(nums)
        if k in s: return len(s)-1
        else: return len(s)
