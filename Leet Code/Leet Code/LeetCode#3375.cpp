class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int a[101]={};
        int N=nums.size();
        int ans=0;
        for(int i=0; i<N; i++){
            int now=nums[i];
            if(now<k) return -1;
            if(now>k){
                if(a[now]==0) ans++;
                a[now]++;
            }
        }
        return ans;
    }
};
