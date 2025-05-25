## LeetCode 2962. Count Subarrays Where Max Element Appears at Least K Times
## �Ƥ@�ơA���h�ֺ� subarray �̭��� nums ���̤j�ȡu�X�{ K ���v
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = tail = times = 0
        ## ���סB����Ϊ����ڡB�X�{�u�̤j�ȡv������

        maximum = max(nums) ## �̤j��

        for head in range(len(nums)):   ## ����Ϊ��Y�A�C�C���k��

            if nums[head] == maximum: times += 1 ## �Y��u�̤j�ȡv
            while times >= k:   ## �Ʊ����Χ��ڦb�u��n���� K �ӡv�B

                if nums[tail] == maximum: times -= 1 ## �R�X�̤j��
                tail += 1   ## ���ک��k�Y

            ans += tail ## ���ڦb�u��n���� K �ӡv�A0...tail-1 ���캡�� k ��
        return ans
