## LeetCode 781. Rabbits in Forest
## �˪L�̤]���P�C�⪺�ߤl�A�ݤ��P�ߤl�u�٦��X���M�A�P��v?
## �з� answers ���^�СA���z�X�u�˪L�̤֦��X���ߤl�v
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers) ## �έp�^�����ƶq
        ans = 0
        for c in counter: ## ���n�^�� c ���i��P��A���� c+1 ���ߤl
            ## �i�� c + 1 ���ߤl�A���Y�Ӧh�A�n�A�����X�s�A�C�s c + 1 �ߤl
            Q = counter[c] // (c + 1) ## ���k���Ӽ�
            M = counter[c] % (c + 1) ## ���k���l��
            ans += (c + 1) * Q ## �i�঳ Q �s
            if M>0: ans += (c + 1) ## ���Y���l�ơA�A�[ 1 �s
        return ans
