## LeetCode 2799. Count Complete Subarrays in an Array
## ��Ӱ}�C�Y�� K �ؤ��P���ơA�����X�� subarray ��n K �ؤ��P����
## �i�Ρu����Ρvsliding window �Ӹѳo�@�D

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        K = len(set(nums)) ## �����R�A��Ӱ}�C�A�� K �ؤ�����
        counter = Counter()
        ans = 0
        tail =0 ## ���䪺���ڡA�|�R�X��
        for head in range(len(nums)): ## �k�䪺�Y�A�|�Y�J��
            counter[nums[head]] += 1

            while len(counter) >= K: ## �u�n�Ʀr�����h
                counter[nums[tail]] -= 1
                if counter[nums[tail]] == 0: ## �Y�ƭY�R�� 0
                    del counter[nums[tail]] ## �N�L����
                tail += 1
            ## �{�b tail...head ���ȡA�u��n���� K �ءv
            ans += tail ## �����ک� 0...tail-1 ���O�X�z��
        return ans
