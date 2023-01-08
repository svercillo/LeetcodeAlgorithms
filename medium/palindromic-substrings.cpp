// A hash function used to hash a pair of any kind
struct hash_pair {
    size_t operator()(const pair<int, int>& p) const
    {
        auto hash1 = hash<int>{}(p.first);
        auto hash2 = hash<int>{}(p.second);
 
        if (hash1 != hash2) {
            return hash1 ^ hash2;             
        }
         
        // If hash1 == hash2, their XOR is zero.
          return hash1;
    }
};

class Solution {
public:
    int countSubstrings(string s) {
        
        int n = s.size();
        
        vector<vector<bool>> dp;
        
        for (int i =0 ; i<n; i++){
            vector<bool> row;
            for (int j =0; j<n; j++){
                row.push_back(false);
            }
            dp.push_back(row);
        }    
        int count = 0;
        for (int i =0; i < n; ++i){
            if (i < n- 1){
                dp[i][i +1] = s[i] == s[i+1];
                if (dp[i][i +1]) count ++;
            }
            dp[i][i] = true; 
            count ++;
        }
        
        for (int k = 3; k <= n; ++k){
            for (int i=0; i <= n - k ; ++i){
                int j = i + k -1;
                dp[i][j] = dp[i+1][j-1] && s[i] == s[j];
                if (dp[i][j]) count ++;
            }
        }
        return count; 
    }
};
