/// LeetCode 73. Set Matrix Zeroes
/// �}�C matrix �̭Y matrix[i][j]==0 ���ܡA�N�����������B���A���ܦ�0
/// �i�H���b����B�W���A�ǳ� 2 ���������}�C�A�Y matrix[i][j]==0 �N�� left[i] �M up[j] ���Ĥ�
/// �̫�A�ΰj��A�⦳���ĤĪ�������l�A���]�� 0 �Y�i

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size(); /// ��M�B�kN
        vector<int> left(M), up(N); /// ��������B�W�������� C++ �}�C
        for(int i=0; i<M; i++){ /// ���� i �d��O M
            for(int j=0; j<N; j++){ /// �k�� j �d��O N
                if(matrix[i][j]==0){ /// �J�즳 0�A�N�b�������B�W���������Ĥ�
                    left[i]=7; /// ���Ĥ�
                    up[j]=7; /// ���Ĥ�
                }
            }
        }
        for(int i=0; i<M; i++){ /// ���� i �d��O M
            for(int j=0; j<N; j++){ /// �k�� j �d��O N
                if(left[i]==7 || up[j]==7) matrix[i][j] = 0;
            } /// �J�쥪�䦳�Ĥ� or �W�����ĤġA�N�⥦�]�� 0
        }
    }
};
