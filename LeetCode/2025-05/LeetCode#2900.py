## LeetCode 2900. Longest Unequal Adjacent Groups Subsequence I
## word[i] ������ Group �O group[i] �i��O 0 or 1
## ��X groups �u����v���u�̪��vsubsequence�A�N�����q��0�Ӷ}�l�Y�i

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [0] ## �̭���uindex�v�A�@�w�i�H��u�̫e���v��0��
        for i in range(1, len(words)): ## �᭱�̧��ˬd
            if groups[ans[-1]] != groups[i]: ## �u�n���P group
                ans.append(i) ## �N�i�H�[�i�h
        return [words[i] for i in ans] ## �A�� ans �̪� i ��X�ӡA�ܦ������� words[i]
