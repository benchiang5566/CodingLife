## LeetCode 1534. Count Good Triplets
## arr �}�C���A�D�� arr[i] arr[j] arr[k]�A3�ƶ����Z���n <== a, b, c �ݦ��X��?

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for i in range(N): ## �N�����ɤO3�h�j��A�����O�L�Y�i�C
            for j in range(i+1, N):
                for k in range(j+1, N):
                    ii, jj, kk = arr[i], arr[j], arr[k] ## �h�g�o�@��A�קK���U�@��L��
                    if abs(ii-jj)<=a and abs(jj-kk)<=b and abs(ii-kk)<=c:
                        ans += 1 ## �ŦX�u�Z�����W�L�d��v�N +1
        return ans

