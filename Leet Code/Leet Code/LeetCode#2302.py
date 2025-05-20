## LeetCode 2302. Count Subarrays With Score Less Than K
## nums ���X�� subarray �̭����u�ӼƬۥ[�A�A������ < k�v

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = total = tail = 0 ## ��l��
        for head in range(len(nums)):
            total += nums[head] ## �k���Y�Y 1 �Ӽ�
            while total * (head - tail+1) >= k: ## �Y���X�Ӫ��ƤӤj
                total -= nums[tail] ## ������ڦR 1 �Ӽ�
                tail += 1 ## ���ʧ��ڪ��ƥ�
            ans += head - tail+1 ## �k�ݬO head�A����i�H�O tail...head
            ## �@�W�[ head - tail+1 �إi��
        return ans
