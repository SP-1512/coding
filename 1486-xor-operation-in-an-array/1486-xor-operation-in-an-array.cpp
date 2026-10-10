class Solution {
public:
    int xorOperation(int n, int start) {
        int nums[n];
        int ans;
        for(int i=0;i<n;i++){
            nums[i] = start + 2 * i;
        }
        ans = nums[0];
        for(int i=1;i<n;i++){
            ans ^= nums[i];
        }
        return ans;
    }
};