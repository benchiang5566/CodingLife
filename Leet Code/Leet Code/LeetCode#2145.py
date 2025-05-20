## LeetCode 2145. Count the Hidden Sequences
## differences ���۾F���Ʀr���t hidden[i+1] - hidden[i]
## �Ʊ� hidden ���� lower ... upper �d�򤺡A���X�إi�઺ hidden �}�C?

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        now = nowLower = nowUpper = 0 ## �ΨӼ����� now �ι����� lower upper �d��
        for d in differences: ## �q 0 �}�l�A�̧Ǽ����u�[�[���v���L�{
            now += d ## ��s now
            nowLower = min(nowLower, now) ## ��s now �����ɪ��U��
            nowUpper = max(nowUpper, now) ## ��s now �����ɪ��W��
        nowR = nowUpper - nowLower ## now �����ɪ��d��
        r = upper - lower ## �D�اƱ檺�d��
        if r < nowR: return 0 ## �Y���������d��Ӥj�A�L�k��J�D�ؽd��A�N����
        return r - nowR + 1 ## �i�H�ɤJ�D�ؽd��u�ưʡv���ܡA��X�����u�ưʽd��v���U�إi��
