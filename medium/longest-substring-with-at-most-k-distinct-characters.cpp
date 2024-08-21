class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {

        int l =0;
        int r = 0;
        int n = s.length();
        map<char, int> freq;

        int mlen = 0;
        while (r < n){ 
            char c;

            c = s[r]; 
            freq[c] += 1;


            while (freq.size() > k){
                c = s[l];
                freq[c] --;

                if (freq[c] == 0){
                    freq.erase(c);
                }

                l ++;
            }

            mlen = max(mlen, r +1 -l);
            r ++;
        }   
        return mlen;
    }
};
