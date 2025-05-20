## LeetCode 2563. Count the Number of Fair Pairs
## �Y Lower <= nums[i] + nums[j] <= upper �s  fair pair�A�`�@���X��?
## ��ı�� 2 �h for �j��A�� nums �� 15^5 �Ӥj�A����� 2 �h�j��C
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() ## Hint 1 ��ĳ sort() �] sort �᪺���L�@�˦h
        ## �A�ӴN²��F�A �� for �j��A�M�w�k��ɡA�A binary search �ݥ��䪺�d��
        ans = 0
        for i in range(1, len(nums)):
            ## �ק� binary search ���ѼơA���n�� nims[:i] �Y�[�t
            j_left = bisect_left(nums, lower - nums[i], hi = i)
            j_right = bisect_right(nums, upper - nums[i], hi = i)
            ans += j_right - j_left
        return ans
