## LeetCode 1920. Build Array from Permutation
## �D�ػ� ans[i] = nums[nums[i]] �N�ӵۼg�A�N�n�F

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        ## �Q�έ˸˥y�A��C�� i ������ num[nums[i]] �ǳƦn�A�N���\�F
