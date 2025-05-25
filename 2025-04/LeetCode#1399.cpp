/// LeetCode 1399. Count Largest Group

class Solution {
public:
    int countLargestGroup(int n) {
        int max_count = 0; /// �Ƥ@�U�A�έp�̦h���A�O�X�{�X��
        int a[100] = {}; /// �}�C�ŧi�A��u�[�`��total�v���X�{�X��
        for(int i=1; i<=n; i++){ /// �H���� for �j��A�q 1...n
            int total = 0, now = i; /// �[�_�Ӫ����G�s total�A�{�b���� now
            while(now > 0){ /// ��֪k�A�p�G now �٦��ѡA�~���
                total += now % 10; /// ��u�֡v�[�_�� (�C�@��ƥ[�_��)
                now = now / 10; /// �駹�֡A�Ʀr�N�ܤp
            }
            a[total]++; /// �έp���G�h 1 �� total ���[�_�Ӫ��� total ���ӥ�
            if(a[total] > max_count) max_count = a[total]; /// max_count ��̦h����
        }
        int ans = 0; /// �̫�䵪�ק�X�� (�X�{�̦h���ƪ����ơA���X�Ӽ�)

        for(int i=0; i<100; i++){ /// ���@�U�}�C a[i] �̭��A��n�O�̤j�� max_count ����
            if(a[i] == max_count) ans++; /// �N�h�@�ӳ̤j����
        }
        return ans;
    }
};
