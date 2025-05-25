## LeetCode 2179. Count Good Triplets in an Array
## nums1 nums2 �̳��� 1...n-1 �o�ǼơA�u�O���s�ƦC�L
## �D x, y, z �T�ơA�Ʊ��n��Ӱ}�C�u������ index �v�����W�A���X�جD�k?
## �]�Ʀr�ܦh 10^5 �A����ΤӦh�j��CHint ���D�n y �i�� binary search �䥪��X�ءB�k��X��

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        index2={num: i for i, num in enumerate(nums2)} ## nums2 �� index ��Ӫ�
        ans1, ans2 = [], [] ## ���O���u���䦳�X�إi��v�B�u�k�䦳�X�إi��v���ݡu�v�@�ۭ��v
        front = [] ## �̧ǩ� nums2 ������ index (�B�H�ɫO���ƧǡA��K�G���j�M)
        for num in nums1: ## nums1 ����k�A�̧ǳB��
            i2 = index2[num] ## nums1 ���o�ӼơA���� nums2[i2]
            idx = bisect_left(front,i2) ## �G���j�M�k�A��� i2 �n��b front ������
            front.insert(idx, i2) ## (1) �N i2 ���J front[idx]�A�� front �O���u�Ƨǡv
            ans1.append(idx) ## (2) idx ��m�M�w�u���䦳�X�إi��v�A�]���� index ���u��p�v

        back = [] ## �˵۩� nums2 ������ index (�B�H�ɫO���ƧǡA��K�G���j�M)
        for num in nums1[::-1]: ## nums1�u�k�쥪�v�̧ǳB�z
            i2 = index2[num] ## nums1 ���o�ӼơA���� nums[i2]
            idx = bisect_left(back, i2) ## �G���j�M

            back.insert(idx, i2) ## (1) �N i2 ���J back[idx]�A�� back �O���u�Ƨǡv
            ans2.append(len(back) - 1 - idx) ## idx ��m�M�w�u�k��v���X�إi��

        ans2 = ans2[::-1] ## �]�j���۳B�z�A�ҥH�n��ӤϹL��
        return sum(a*b for a, b in zip(ans1, ans2)) ## �w�襤�� y ���y�СA�N ans1[i] * ans2[i]
