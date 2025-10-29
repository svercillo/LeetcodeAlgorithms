class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        
        int l =0;
        int r = 0;
        int n = s.length();

        map<char,int> freq;
        int maxLen = 0;
        while (r < n){
            char c = s[r];

            freq[c] = freq[c] + 1;
            
            while (freq.size() > 2){
                c = s[l];
                if (freq.find(c) != freq.end()){
                    freq[c] = freq[c] - 1;
                    
                    if (freq[c] == 0){
                        freq.erase(c);
                    }
                }
                
                
                l++;
            }

            maxLen = max(maxLen, r +1 - l);
            r++;
        }

        return maxLen;
    }
};
