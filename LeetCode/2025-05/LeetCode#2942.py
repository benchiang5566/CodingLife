## LeetCode 2942. Find Words Containing Character
## words �̡A�����Ǧr�u�t�� x �r��?�v ������� index i ��X��
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)): ## �w�� words �̪��C�Ӧr
            if x in words[i]: ans.append(i) ## �Y�t���r�� x�A�N�[�쵪�׸�
        return ans
