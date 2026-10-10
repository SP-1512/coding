class Solution {
public:
    int subtractProductAndSum(int n) {
        int pro = 1 ,sub = 0;
        while(n!=0){
            int rem = n%10;
            pro *= rem;
            sub += rem;
            n = n/10;
        }
        return (pro - sub);
    }
};