## LeetCode 3362. Zero Array Transformation III
## queries �� [left, right] �i�N nums[left]..nums[right] �D�Ǽơu�� 1�v
## �Ʊ� nums ������ܦ� 0, �� queries ���Ǩ��u�R�����Ρv�]��F������:�̦h�i�u�R���X��?�v
## ����:���� queries �ƧǡA�A�� heap �v�@�P�_ num[i]�u�O�_��Ρv�u�O�_�ݭn�v�Y�� queries ����

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(reverse = True) ## Hint 1�Ƨ�(�N�� pop() ���X�A�ҥH�u�ϹL�ӡv �p���b�k��)
        ## Hint 2 ���D query�u�����ɶ��������v�]�u�]�t���d����j�v�A�ҥH�ϥ� 2 �� heap
        heapAvailable = [] ## �ثe�u�d�򦳮ġv�u��Ϊ� query�v�C�p��!!�����ɶ��ߪ��u��(heapAvailable �[�t��)
        heapUsing = [] ## �u���b�ϥΡv�� query�A�b heap �O���L���u�����ɶ��v(�L�����|����)
        for i in range(len(nums)): ## �̧ǳB�z nums[i]
            while queries and queries[-1][0] <= i: ## ��u�}�l�v�b i ���e�u��Ϊ� query�v
                left, right = queries.pop() ## �����X�A��U heapAvailable ��
                heappush(heapAvailable, -right) ## �O�U�����ɶ��C�u�����ɶ��v�V�᭱�V�n (heapAvailable �[�t��)
            while heapUsing and heapUsing[0] < i: ## ��u�����ɶ��v�b i ���e�N���Ī� query
                heappop(heapUsing) ## �N�ᱼ (�L�����|����)
            while nums[i] > len(heapUsing): ## ���b�ϥΪ� query �Y�ƶq����
                if len(heapAvailable) == 0: return -1 ## �S���u��Ϊ� query�v�A����
                if i > -heapAvailable[0]: return -1 ## �ɶ������W(�����ɶ��S��t i) �A����(heapAvailable �[�t��)
                biggestEnding = -heappop(heapAvailable) ## �D�u�̻��~�����v�ӥ�(heapAvailable �[�t��)
                heappush(heapUsing, biggestEnding) ## ���ӥ�
        return len(heapAvailable) ## �٨S�Ϊ��B�ٳѤU�Ӫ��B�i�`�٤U�Ӫ� query
