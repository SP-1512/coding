class Solution {
public:
    int minDeletions(string s) {
        map <char, int> Map1;
        map <int, int> Map2;
        
        for(auto i : s){
            Map1[i]++;
        }
        int cnt = 0;
        for(auto j : Map1){
            if(Map2[j.second] == 0){
                Map2[j.second]++;
            }
            else{
                int c = j.second;
                while(Map2[c] != 0) {
                    cnt++;
                    c--;
                }
                if(c >0) Map2[c]++;
            }

            cout << cnt << endl; 
        }
        return cnt;
    }
};