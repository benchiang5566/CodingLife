## LeetCode 2131. Longest Palindrome by Concatenating Two Letter Words
## �Q�� words �̡u�\�h 2 �Ӧr�����r��v�զX�X�u�̪��� Palinedrom �j��v����
## 2131 ���@�\�h�u2�Ӧr���v�p�r�� words �}�C�A��γo�ǡu�եX�̪����j��v�����צ��h���C

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)    ## ���N words �̪��r�A�έp������
        ans = 0 ## �j�媺����
        center = 0  ## �����Y��u2 �ӬۦP�r���v�A��^�m��?
        for w in counter:   ## �w��ثe�����r
            if w[0]==w[1]:  ## 2 �ӬۦP�r���A�i��j�夤���A�]�i�P�ۤv�t��
                ans += counter[w]// 2*4 ## ���ƪ������A�i��٩�
                if counter[w]%2==1: center = 2  ## �i��b������ 2 �Ӧr��
            elif counter[w]>0 and counter[w[1]+w[0]] > 0:   ## ���B�Ϫ��r���s�b
                now = min(counter[w], counter[w[1]+w[0]])   ## �i�t�X now ��
                ans += 4*now    ## �� 2 �Ӧr���B�k 2 �Ӧr���A�@ 4 �Ӧr��
                counter[w] -= now   ## �α� now ��
                counter[w[1]+w[0]] -= now   ## �α� now ��
        return ans + center ## ��եX�u�j��v���̪�����
